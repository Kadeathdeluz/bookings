# -*- coding: utf-8 -*-

from odoo import models, fields

class Pack(models.Model):
    """
    Model that represents a Pack (of items or/and services).
    """
    _name = 'bookings.pack'
    _description = 'Represents a pack of the Camino de Santiago experience with items and/or services included'

    # Table fields
    name = fields.Char()
    descripcion = fields.Text()