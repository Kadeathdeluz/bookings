# -*- coding: utf-8 -*-

from odoo import models, fields

class Pack(models.Model):
    """
    Model that represents a Pack (of items or/and services).
    """
    _name = 'bookings.pack'
    _description = 'Represents a pack of the Camino de Santiago experience with items and/or services included'

    # -- Table fields --
    # PK: pack_id1
    # pack_id = fields.Char() <-- Not needed

    # Other table fields
    name = fields.Char()
    price = fields.Float()
    description = fields.Text()

    # -- Relations --
    # One2many with lodgin_by_pack
    related_lodgins_ids = fields.One2many('bookings.lodgin_by_pack', 'pack_id', string= ' Lodgins by Pack')
    # One2many with item_by_pack
    related_items_ids = fields.One2many('bookings.item_by_pack', 'pack_id', string= ' Items by Pack')