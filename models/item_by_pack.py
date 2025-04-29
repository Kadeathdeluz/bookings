# # -*- coding: utf-8 -*-

# from odoo import models, fields

# class ItemByPack(models.Model):
#     """
#     Model that represents an item belongs to a pack.
#     """
#     _name = 'bookings.item_by_pack'
#     _description = 'Represents the relation between an item and a pack'

#     # -- Relations --
#     # Many2one with item
#     item_id = fields.Many2one('bookings.item', string='Item')
#     # Many2one with pack
#     pack_id = fields.Many2one('bookings.pack', string='Pack')