# -*- coding: utf-8 -*-

from odoo import models, fields

class Item(models.Model):
    """
    Model that represents an item of the Camino de Santiago experience.
    """
    _name = 'bookings.item'
    _description = 'Represents an item of the Camino de Santiago experience'

    # Table fields
    name = fields.Char()
    descripcion = fields.Text()