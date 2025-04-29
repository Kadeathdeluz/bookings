# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Journey(models.Model):
    """
    Model that represents a Journey for a client, related to a route, and a pack.
    """
    _name = 'bookings.journey'
    _description = 'Represents a journey of the Camino de Santiago for a client, related to a route, and a pack'

    # -- Table fields --
    name = fields.Char()
    date = fields.Date()
    with_pet = fields.Boolean()
    mobility_reduced = fields.Boolean()
    # A selection of available states
    state = fields.Selection([
        ('pending', 'Pending'),
        ('finished', 'Finished'),
        ('progress', 'In Progress')
    ], string= 'Status', default='pending')

    # -- Calculated fields --
    # Number of lodgins by journey
    lodgins_count = fields.Integer(
        string=' Lodgins Count', 
        compute= '_compute_lodgins_count',
        store= True
        )

    # -- Relations --
    # FKs: client_id, route_id, pack_id and the date
    client_id = fields.Many2one('bookings.client', string= ' Client')
    route_id = fields.Many2one('bookings.route', string= ' Route')
    pack_id = fields.Many2one('bookings.pack', string= ' Pack')

    # One2many with lodgin_by_journey
    related_lodgins_ids = fields.One2many('bookings.lodgin_by_journey', 'journey_id', string= ' Lodgins by Journey')

    # -- Constraints --
    # client_id, route_id, pack_id and date must be unique together
    # _sql_constraints = [
    #     ('unique_journey_by_date', 'unique(client_id, route_id, pack_id, date)', 'The combination of client, route pack and date must be unique.')
    # ]

    # -- Functions --
    # Returns the number of lodgins related to a journey
    @api.depends('related_lodgins_ids')
    def _compute_lodgins_count(self):
        for rec in self:
            rec.lodgins_count = len(rec.related_lodgins_ids)
