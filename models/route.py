# -*- coding: utf-8 -*-

from odoo import models, fields

class Route(models.Model):
    """
    Model that represents a route of the Camino de Santiago.
    """
    _name = 'bookings.route'
    _description = 'Represents a route of the Camino de Santiago'

    # Table fields
    name = fields.Char()
    descripcion = fields.Text()