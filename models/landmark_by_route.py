# -*- coding: utf-8 -*-

from odoo import models, fields

class LandmarkByRoute(models.Model):
    """
    Model that represents the lodgin by route of the Camino de Santiago.
    """
    _name = 'bookings.landmark_by_route'
    _description = 'Represents a landmark in a route'
    
    # -- Table fields --
    order_in_route = fields.Integer(string='Order in route')

    # -- Relations --
    # FK: route_id (not the route_id of the route table, but the internal id of the route table)
    route_id = fields.Many2one(
        comodel_name='bookings.route', 
        string='Route', 
        ondelete= 'cascade')
    # FK: landmark_id (references internal id of landmark table)
    landmark_id = fields.Many2one(
        comodel_name='bookings.landmark', 
        string='Landmark', 
        ondelete= 'cascade')
    
    # -- Constraints --
    # order_in_route must be unique for each route_id
    # _sql_constraints = [
    #     ('order_in_route_UK', 'unique(route_id, order_in_route)', 'Order in route must be unique for each route')
    # ???
    # ]