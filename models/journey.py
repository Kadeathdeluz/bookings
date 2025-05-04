# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
    ], string= 'Status', default='pending')

    # -- Calculated fields --
    # Number of lodgins by journey
    lodgins_count = fields.Integer(
        string=' Lodgins (count)', 
        compute= '_compute_lodgins_count',
        store= True
        )

    # -- Relations --
    client_id = fields.Many2one('bookings.client', string= ' Client')
    route_id = fields.Many2one('bookings.route', string= ' Route')
    pack_id = fields.Many2one('bookings.pack', string= ' Pack')
    
    # Related lodgins to the current journey
    related_lodgins_ids = fields.Many2many(
        comodel_name='bookings.lodgin',
        relation='bookings_lodgin_by_journey',
        column1='journey_id',
        column2='lodgin_id',
        string='Lodgins'
    )

    # -- Constraints --
    # Fields client_id, route_id, pack_id and date must be unique (together)
    _sql_constraints = [
        ('journey_UK', 'unique(client_id, route_id, pack_id, date)', 'Fields client_id, route_id, pack_id and date must be unique together.')
    ]

    # -- Functions --
    # Returns the number of lodgins related to a journey
    @api.depends('related_lodgins_ids')
    def _compute_lodgins_count(self):
        for rec in self:
            rec.lodgins_count = len(rec.related_lodgins_ids)
