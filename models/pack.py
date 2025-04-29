# -*- coding: utf-8 -*-

from odoo import models, fields

class Pack(models.Model):
    """
    Model that represents a Pack (of items or/and services).
    """
    _name = 'bookings.pack'
    _description = 'Represents a pack of the Camino de Santiago experience with items and/or services included'

    # -- Table fields --
    name = fields.Char()
    price = fields.Float()
    description = fields.Text()

    # -- Relations --
    # One2many with lodgin_by_pack
    related_lodgins_ids = fields.One2many('bookings.lodgin_by_pack', 'pack_id', string= ' Lodgins by Pack')
    # One2many with item_by_pack
    #related_items_ids = fields.One2many('bookings.item_by_pack', 'pack_id', string= ' Items by Pack')
    
    # Related items to the current pack
    related_items_ids = fields.Many2many(
        comodel_name='bookings.item',                      # Related model
        relation='bookings_item_by_pack',                  # Actual name of the many2many table
        column1='pack_id',                                 # Column towards this model
        column2='item_id',                                 # Column towards the destination model
        string='Includes'                               # Name of the field in the view
    )
    # -- Functions --
    # Returns the name of the Pack
    def name_get(self):
        return [(rec.id, rec.name) for rec in self]