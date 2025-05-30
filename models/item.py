# -*- coding: utf-8 -*-

from odoo import models, fields

class Item(models.Model):
    """
    Model that represents an item of the Camino de Santiago experience.
    """
    _name = 'bookings.item'
    _description = 'Represents an item of the Camino de Santiago experience'

    # -- Table fields --
    name = fields.Char(string='Name', required=True)
    price = fields.Float(string='Price', required=True)
    description = fields.Text(string='Description')

    # -- Relations --
    # Packs that include this item
    related_pack_ids = fields.Many2many(
        comodel_name='bookings.pack',                      
        relation='bookings_item_by_pack',                  
        column1='item_id',                                 
        column2='pack_id',                                 
        string='Packs'                                     
    )