# -*- coding: utf-8 -*-

from odoo import models, fields

class Lodgin(models.Model):
    """
    Model that represents a Lodging of a route.
    """
    _name = 'bookings.lodgin'
    _description = 'Represents a lodging that can be booked following a route of the Camino de Santiago with a concrete pack'

    # -- Table fields --
    name = fields.Char()
    capacity = fields.Integer()
    pets_allowed = fields.Boolean()
    reduced_mobility = fields.Boolean()
    phone = fields.Char()
    email = fields.Char()
    description = fields.Text()

    # -- Relations --
    # One2many with lodgin_by_route
    related_routes_ids = fields.One2many('bookings.lodgin_by_route', 'lodgin_id', string= ' Lodgins by Route')
    # One2many with lodgin_by_pack
    related_packs_ids = fields.One2many('bookings.lodgin_by_pack', 'lodgin_id', string= ' Lodgins by Pack')
    # One2many with lodgin_by_journey
    related_journeys_ids = fields.One2many('bookings.lodgin_by_journey', 'lodgin_id', string= ' Lodgins by Journey')