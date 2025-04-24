# -*- coding: utf-8 -*-

from odoo import models, fields

class Client(models.Model):
    """
    Model that represents a client of the Camino de Santiago experience.
    """
    #_inherit = 'res.partner'
    _name = 'bookings.client'
    _description = 'Represents a client of the Camino de Santiago experience'

    # Table fields
    # client_id = fields.Char() <-- Not needed
    name = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    born_date = fields.Date()

    # -- Relations --
    # One2many with journey
    related_journeys_ids = fields.One2many('bookings.journey', 'id', string= ' Journeys by Client')