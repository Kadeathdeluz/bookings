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
    pointX = fields.Char(string='Longitude', required=True)
    pointY = fields.Char(string='Latitude', required=True)
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
    # order_in_route = fields.Integer() -> En realidad es un atributo de la tabla intermedia
    description = fields.Text(string='Description')

    # -- Relations --
    # One2many with landmark_by_route
    related_routes_ids = fields.One2many('bookings.landmark_by_route', 'landmark_id', string= ' Landmarks by Route')

    # -- Constraints --
    # pointX, pointY and type fields must be unique (together)
    # _sql_constraints = [
    #     ('pX_pY_type_UK', 'unique(pointX, pointY, type)', 'Combination of Long-Lat with type must be unique.')
    # ]

    # -- Functions --
    # Returns the name of the Route
    def name_get(self):
        return [(rec.id, rec.name) for rec in self]