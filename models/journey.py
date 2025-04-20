# -*- coding: utf-8 -*-

from odoo import models, fields

class Journey(models.Model):
    """
    Model that represents a Journey for a client, related to a route, a pack and lodgings.
    """
    _name = 'bookings.journey'
    _description = 'Represents a journey of the Camino de Santiago for a client, related to a route, a pack and lodgings'

    # Table fields
    name = fields.Char()
    descripcion = fields.Text()