# -*- coding: utf-8 -*-

from odoo import models, fields

class Lodgin(models.Model):
    """
    Model that represents a Lodging of a route.
    """
    _name = 'bookings.lodgin'
    _description = 'Represents a lodging that can be booked following a route of the Camino de Santiago with a concrete pack'

    # -- Table fields --
    cif = fields.Char(string='CIF', required=True)
    name = fields.Char(string='Name', required=True)
    capacity = fields.Integer(string='Capacity', required=True)
    pets_allowed = fields.Boolean(string='Pets allowed')
    reduced_mobility = fields.Boolean(string='Reduced mobility')
    phone = fields.Char(string='Phone', required=True)
    email = fields.Char(string='Email', required=True)
    description = fields.Text(string='Description')

    # -- Relations --
    # Related routes to the current lodgin
    related_routes_ids = fields.Many2many(
        comodel_name='bookings.route',
        relation='bookings_lodgin_by_route',
        column1='lodgin_id',
        column2='route_id',
        string='Routes'
    )

    # Related packs to the current lodgin
    related_packs_ids = fields.Many2many(
        comodel_name='bookings.pack',
        relation='bookings_lodgin_by_pack',
        column1='lodgin_id',
        column2='pack_id',
        string='Packs'
    )

    # Related journeys to the current lodgin
    related_journeys_ids = fields.Many2many(
        comodel_name='bookings.journey',
        relation='bookings_lodgin_by_journey',
        column1='lodgin_id',
        column2='journey_id',
        string='Journeys'
    )
    
    # -- Constraints --
    # cif must be unique
    _sql_constraints = [
        ('cif_UK', 'unique(cif)', 'CIF must be unique.')
        ]