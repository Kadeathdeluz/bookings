# -*- coding: utf-8 -*-

from odoo import models, fields

class Landmark(models.Model):
    """
    Model that represents a landmark of a route in the Camino de Santiago.
    """
    _name = 'bookings.landmark'
    _description = 'Represents a landmark of a route in the Camino de Santiago'

    # -- Table fields --
    name = fields.Char(string='Name', required=True)
    point_x = fields.Char(string='Longitude', required=True)
    point_y = fields.Char(string='Latitude', required=True)
    # A selection of landmark types
    type = fields.Selection(selection=[
        ('cultural', 'Cultural'),
        ('natural', 'Natural'),
        ('historical', 'Historical'),
        ('religious', 'Religious'),
        ('gastronomic', 'Gastronomic'),
        ('other', 'Other')
    ], string='Type'
    , required=True)
    description = fields.Text(string='Description')

    # -- Relations --
    # Related routes
    related_routes_ids = fields.One2many('bookings.landmark_by_route', 'landmark_id', string= ' Routes')

    # -- Constraints --
    # point_x, point_y and type fields must be unique (together)
    _sql_constraints = [
        ('px_py_type_uk', 'unique(point_x, point_y, type)', 'Combination of Longitude, Latitude, and Type must be unique.')
    ]

    # -- Functions --
    # Returns the name of the Route
    def name_get(self):
        return [(rec.id, rec.name) for rec in self]