# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Client(models.Model):
    """
    Model that represents a client of the Camino de Santiago experience.
    """
    #_inherit = 'res.partner'
    _name = 'bookings.client'
    _description = 'Represents a client of the Camino de Santiago experience'

    # Table fields
    dni = fields.Char(string='DNI',required=True)
    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone', required=True)
    email = fields.Char(string='Email', required=True)
    born_date = fields.Date(string='Born date', required=True)

    # -- Relations --
    # Related journeys to the current client
    related_journeys_ids = fields.One2many(
        comodel_name='bookings.journey', 
        inverse_name='client_id', 
        string= 'Journeys')

    # -- Constraints --
    # dni field must be unique
    _sql_constraints = [
        ('dni_UK', 'unique(dni)', 'DNI must be unique.')
    ]