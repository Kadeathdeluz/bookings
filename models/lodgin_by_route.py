# -*- coding: utf-8 -*-

from odoo import models, fields

class LodginByRoute(models.Model):
    """
    Model that represents a lodgin that can be found in a route.
    """
    _name = 'bookings.lodgin_by_route'
    _description = 'Represents a lodgin that can be found in a route'

    # -- Table fields --
    # FK: route_id (not the route_id of the route table, but the internal id of the route table)
    route_id = fields.Many2one('bookings.route', string='Route')
    # FK: lodgin_id (references internal id of lodgin table)
    lodgin_id = fields.Many2one('bookings.lodgin', string='Lodgin')