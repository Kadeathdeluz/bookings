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
    name = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    born_date = fields.Date()

    # -- Relations --
    # One2many with journey
    related_journeys_ids = fields.One2many('bookings.journey', 'id', string= ' Journeys by Client')

    # -- Constraints --
    # name and born_date fields must be unique (together)
    # _sql_constraints = [
    #     ('name_born_UK', 'unique(name, born_date)', 'Combination of Name and Born Date must be unique.')
    # ]