# -*- coding: utf-8 -*-

from odoo import models, fields

class Landmark(models.Model):
    """
    Model that represents a landmark of a route in the Camino de Santiago.
    """
    _name = 'bookings.landmark'
    _description = 'Represents a landmark of a route in the Camino de Santiago'

    # -- Table fields --
    # PK: pointX, pointY
    pointX = fields.Float(string='Longitude', required=True)
    pointY = fields.Float(string='Latitude', required=True)
    
    # Other table fields
    # A selection of landmark types
    type = fields.Selection(selection=[
        ('cultural', 'Cultural'),
        ('natural', 'Natural'),
        ('historical', 'Historical'),
        ('religious', 'Religious'),
        ('gastronomic', 'Gastronomic'),
    ], string='Type')
    # order_in_route = fields.Integer() -> En realidad es un atributo de la tabla intermedia
    description = fields.Text()

    # -- Relations --
    # One2many with landmark_by_route
    related_routes_ids = fields.One2many('bookings.landmark_by_route', 'landmark_id', string= ' Landmarks by Route')

    # -- Constraints --
    # pointX and pointY fields must be unique (together)
    # _sql_constraints = [
    #     ('pointX_pointY_UK,', 'unique(pointX, pointY)', 'Combination of Long and Lat must be unique (PK)')
    # ]