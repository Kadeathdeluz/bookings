# -*- coding: utf-8 -*-

from odoo import models, fields

class Lodgin(models.Model):
    """
    Model that represents a Lodging of a route.
    """
    _name = 'bookings.lodgin'
    _description = 'Represents a lodging that can be booked following a route of the Camino de Santiago with a concrete pack'

    # Table fields
    name = fields.Char()
    descripcion = fields.Text()