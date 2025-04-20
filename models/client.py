# -*- coding: utf-8 -*-

from odoo import models, fields

class Client(models.Model):
    """
    Model that represents a client of the Camino de Santiago experience.
    """
    _name = 'bookings.client'
    _description = 'Represents a client of the Camino de Santiago experience'

    # Table fields
    name = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    address = fields.Char()
    postal_code = fields.Char()
    city = fields.Char()
    country = fields.Char()