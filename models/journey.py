# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Journey(models.Model):
    """
    Model that represents a Journey for a client, related to a route, and a pack.
    """
    _name = 'bookings.journey'
    _description = 'Represents a journey of the Camino de Santiago for a client, related to a route, and a pack'

    # -- Table fields --
    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Journey Date', required=True)
    with_pet = fields.Boolean(string='With Pet')
    mobility_reduced = fields.Boolean(string='Reduced Mobility')
    # A selection of available status
    state = fields.Selection([
        ('pending', 'Pending'),
        ('finished', 'Finished'),
        ('progress', 'In Progress')
        ], string= 'Status',
        default='pending',
        required=True)
    
    # -- Aux fields --
    booked_lodgins_msg = fields.Char()
    
    # -- Calculated fields --
    # Number of lodgins by journey
    lodgins_count = fields.Integer(
        string=' Lodgins (count)', 
        compute= '_compute_lodgins_count',
        store= True
    )
    # Suitable lodgins depending on the selected route and pack
    suitable_lodgins = fields.Many2many(
        'bookings.lodgin',
        string="Suitable Lodgins",
        compute='_compute_suitable_lodgins',
        store=False
    )

    # -- Relations --
    client_id = fields.Many2one('bookings.client', string= ' Client', required=True)
    route_id = fields.Many2one('bookings.route', string= ' Route', required=True)
    pack_id = fields.Many2one('bookings.pack', string= ' Pack', required=True)
    
    # Related lodgins to the current journey
    related_lodgins_ids = fields.Many2many(
        comodel_name='bookings.lodgin',
        relation='bookings_lodgin_by_journey',
        column1='journey_id',
        column2='lodgin_id',
        string='Lodgins',
    )

    # -- Constraints --
    # Fields client_id, route_id, pack_id and date must be unique (together)
    _sql_constraints = [
        ('journey_UK', 'unique(client_id, route_id, pack_id, date)', 'Fields client_id, route_id, pack_id and date must be unique together.')
    ]

    # -- Functions --   

    # Constraint: Ensures that a journey haves at least one related lodgin
    @api.constrains('related_lodgins_ids')
    def _check_lodgins_not_empty(self):
        for record in self:
            if not record.related_lodgins_ids:
                raise ValidationError("Journey must have at least one related lodgin.") 
    
    # - API DEPENDS -
    @api.depends('related_lodgins_ids')
    # Computes the number of lodgins related to a journey
    def _compute_lodgins_count(self):
        for rec in self:
            rec.lodgins_count = len(rec.related_lodgins_ids)
    
    @api.depends('route_id', 'pack_id', 'with_pet', 'mobility_reduced')
    # Computes the suitable lodgins to a journey
    def _compute_suitable_lodgins(self):
        for journey in self:
            # Without pack &/or route, there are no suitable lodgins
            if not journey.route_id or not journey.pack_id:
                journey.suitable_lodgins = False
                continue # Skip journey
                
            domain = [
                ('id', 'in', journey.route_id.related_lodgins_ids.ids),
                ('id', 'in', journey.pack_id.related_lodgins_ids.ids)
            ]
            if journey.with_pet:
                domain.append(('pets_allowed', '=', True))
            if journey.mobility_reduced:
                domain.append(('reduced_mobility', '=', True))
            
            # Assign suitable lodgins to the field
            journey.suitable_lodgins = self.env['bookings.lodgin'].search(domain)

    # - API ONCHANGE -
    @api.onchange('route_id', 'pack_id', 'with_pet', 'mobility_reduced')
    # Automatized lodgins booking
    def _onchange_autobooking(self):
        if not self.route_id or not self.pack_id:
            return

        if not self.suitable_lodgins:
            self.related_lodgins_ids = False
            self.booked_lodgins_msg = "There are no suitable lodgins with the selected requirements."
            return

        self.related_lodgins_ids = self.suitable_lodgins

        # Just to show the appropiate message
        if len(self.suitable_lodgins) == 1:
            self.booked_lodgins_msg = f"There are {len(self.suitable_lodgins)} suitable lodgin!"
        else:
            self.booked_lodgins_msg = f"There are {len(self.suitable_lodgins)} suitable lodgins!"
        return
    
    # - CRUD operations (modified) -

    @api.model
    # Modified create function
    def create(self, vals):
        record = super(Journey,self).create(vals)
        if record.related_lodgins_ids != record.suitable_lodgins:
            # Incorrect lodgins (or not suitable) are the ones that not in suitable_lodgins
            incorrect_lodgins = record.related_lodgins_ids - record.suitable_lodgins
            
            if incorrect_lodgins:
                # Message to show details of the error
                lodgin_names = ', '.join(incorrect_lodgins.mapped('name'))
                message = (
                    f"The following lodgins aren't suitable for the selected requirements:\n"
                    f" {lodgin_names}\n\n"
                )
                # Finally, before error, assign the correct suitable_lodgins to related lodgins
                record.related_lodgins_ids = record.suitable_lodgins
                # Raises the error to prevent record edition
                raise UserError(message)
            
        return record
    
    # Modified write function 
    def write(self, vals):
        record = super().write(vals)

        # If there are modified fields that are in the requirements, trigger the check of the related_journeys
        trigger_fields = {'route_id', 'pack_id', 'with_pet', 'mobility_reduced', 'related_lodgins_ids'}
        if any(field in vals for field in trigger_fields):
            for journey in self:
                if journey.related_lodgins_ids != journey.suitable_lodgins:
                    incorrect_lodgins = journey.related_lodgins_ids - journey.suitable_lodgins
                    if incorrect_lodgins:
                        # Message to show details of the error
                        lodgin_names = ', '.join(incorrect_lodgins.mapped('name'))
                        message = (
                            f"The following lodgins aren't suitable for the selected requirements:\n"
                            f" {lodgin_names}\n\n"
                        )
                        # Finally, before error, assign the correct suitable_lodgins to related lodgins
                        journey.related_lodgins_ids = journey.suitable_lodgins
                        # Raises the error to prevent record edition
                        raise UserError(message)
                    
                    journey.related_lodgins_ids = journey.suitable_lodgins

        return record
