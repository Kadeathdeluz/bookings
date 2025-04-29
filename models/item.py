# -*- coding: utf-8 -*-

from odoo import models, fields

class Item(models.Model):
    """
    Model that represents an item of the Camino de Santiago experience.
    """
    _name = 'bookings.item'
    _description = 'Represents an item of the Camino de Santiago experience'

    # -- Table fields --
    name = fields.Char()
    price = fields.Float()
    description = fields.Text()

    # -- Relations --
    # One2many with item_by_pack
    related_packs_ids = fields.One2many('bookings.item_by_pack', 'item_id', string= ' Items by Pack')

    # Shows the packs that include this item
    pack_ids = fields.Many2many(
        'bookings.pack',                           # Related model
        'bookings_item_by_pack',                   # Actual name of the many2many table (we use the intermediate one)
        'item_id',                                 # Column towards this model
        'pack_id',                                 # Column towards the destination model
        string='Included in'                       # Name of the field in the view
    )