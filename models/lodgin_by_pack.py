# -*- coding: utf-8 -*-

from odoo import models, fields

class LodginByPack(models.Model):
    """
    Model that represents the relation between a lodging and a pack.
    """
    _name = 'bookings.lodgin_by_pack'
    _description = 'Represents the relation between a lodging and a pack'

    # -- Table fields --
    # -- Relations --
    # FK: lodgin_id
    lodgin_id = fields.Many2one('bookings.lodgin', string= ' Lodgin')
    # FK: pack_id
    pack_id = fields.Many2one('bookings.pack', string= ' Pack')