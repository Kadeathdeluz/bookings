# -*- coding: utf-8 -*-

from odoo import models, fields

class Item(models.Model):
    """
    Model that represents an item of the Camino de Santiago experience.
    """
    _name = 'bookings.item'
    _description = 'Represents an item of the Camino de Santiago experience'

    # -- Table fields --
    # PK: item_id
    # item_id = fields.Char() <-- Not needed

    # Other table fields
    name = fields.Char()
    price = fields.Float()
    description = fields.Text()

    # -- Relations --
    # One2many with item_by_pack
    related_packs_ids = fields.One2many('bookings.item_by_pack', 'item_id', string= ' Items by Pack')