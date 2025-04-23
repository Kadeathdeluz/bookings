# -*- coding: utf-8 -*-

from odoo import models, fields

class Journey(models.Model):
    """
    Model that represents a Journey for a client, related to a route, and a pack.
    """
    _name = 'bookings.journey'
    _description = 'Represents a journey of the Camino de Santiago for a client, related to a route, and a pack'

    # -- Table fields --
    
    # Other table fields
    date = fields.Date()
    name = fields.Char()
    with_pet = fields.Boolean()
    movility_reduced = fields.Boolean()

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

