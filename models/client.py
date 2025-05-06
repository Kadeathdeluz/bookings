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

    # -- Functions --
    # Decorator of a constraint checker
    @api.constrains('dni')
    def _check_dni_letter(self):
        """
        Validates that the DNI has a correct control letter.
        Format: 8 digits + 1 letter (e.g., 12345678Z)
        """
        letters = 'TRWAGMYFPDXBNJZSQVHLCKE' # The order corresponds to [0..22] values
        
        for record in self:
            dni = record.dni.upper()
            # DNI format 8 digits + 1 letter validation
            if len(dni) != 9 or not dni[:8].isdigit() or not dni[8].isalpha():
                raise ValidationError("DNI format must be 8 digits followed by a letter (e.g., 12345678Z).")

            # Control letter value validation
            remainder = int(dni[:8])
            expected_letter = letters[remainder % 23]
            if dni[8] != expected_letter:
                raise ValidationError(f"Incorrect letter of the DNI '{dni}'. It should be '{expected_letter}'.")