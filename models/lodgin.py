# -*- coding: utf-8 -*-

from odoo import models, fields

class Lodgin(models.Model):
    """
    Model that represents a Lodging of a route.
    """
    _name = 'bookings.lodgin'
    _description = 'Represents a lodging that can be booked following a route of the Camino de Santiago with a concrete pack'

    # -- Table fields --
    #cif = fields.Char()
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
        string='Founded in'
    )
    # One2many with lodgin_by_pack
    # related_packs_ids = fields.One2many('bookings.lodgin_by_pack', 'lodgin_id', string= ' Lodgins by Pack')
    # Related packs to the current lodgin
    related_packs_ids = fields.Many2many(
        comodel_name='bookings.pack',
        relation='bookings_lodgin_by_pack',
        column1='lodgin_id',
        column2='pack_id',
        string='Asociated to'
    )
    # One2many with lodgin_by_journey
    related_journeys_ids = fields.One2many('bookings.lodgin_by_journey', 'lodgin_id', string= ' Lodgins by Journey')

    # -- Constraints --
    # cif must be unique
    # _sql_constraints = [
    #     ('dni_UK', 'unique(dni)', 'DNI must be unique.')
    #     ]