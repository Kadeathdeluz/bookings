# -*- coding: utf-8 -*-

from odoo import models, fields

class LodginByJourney(models.Model):
    """
    Definition
    """
    _name = 'bookings.lodgin_by_journey'
    _description = 'Represents a lodgin booked in a journey'

    # -- Table fields --
    # FK: lodgin_id
    lodgin_id = fields.Many2one('bookings.lodgin')
    # FK: journey_id
    journey_id = fields.Many2one('bookings.journey_id')