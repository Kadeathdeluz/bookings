# -*- coding: utf-8 -*-

from odoo import models, fields

class Landmark(models.Model):
    """
    Model that represents a landmark of a route in the Camino de Santiago.
    """
    _name = 'bookings.landmark'
    _description = 'Represents a landmark of a route in the Camino de Santiago'

    # Table fields
    name = fields.Char()
    descripcion = fields.Text()