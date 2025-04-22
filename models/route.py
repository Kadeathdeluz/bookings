# -*- coding: utf-8 -*-

from odoo import models, fields

class Route(models.Model):
    """
    Model that represents a route of the Camino de Santiago.
    """
    _name = 'bookings.route'
    _description = 'Represents a route of the Camino de Santiago'

    # -- Table fields --
    # PK: route_id
    # route_id = fields.Char() <-- Not needed

    # Other table fields
    name = fields.Char()
    distance = fields.Float()
    url_maps = fields.Char()
    description = fields.Text()

    # -- Relations --
    # One2many with landmark_by_route
    related_landmarks_ids = fields.One2many(
        'bookings.landmark_by_route', 'route_id', string= ' Landmarks by Route'
        )
    # One2many with lodgin_by_route
    related_lodgins_ids = fields.One2many(
        'bookings.lodgin_by_route', 'route_id', string= ' Lodgins by Route'
        )

    # -- Constraints --
    # route_id must be unique
    # _sql_constraints = [
    #     ('route_id_uk', 'unique(route_id)', 'Route ID must be unique (PK)')
    # ]