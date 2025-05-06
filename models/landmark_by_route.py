# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LandmarkByRoute(models.Model):
    """
    Model that represents the lodgin by route of the Camino de Santiago.
    """
    _name = 'bookings.landmark_by_route'
    _description = 'Represents a landmark in a route'
    
    # -- Table fields --
    order_in_route = fields.Integer(string='Order in route', readonly="1")

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
        ondelete= 'cascade', required=True)
    
    #-- Calculated fields --
    is_duplicate = fields.Boolean(
        string="Is Duplicate",
        compute='_compute_is_duplicate',
        store=False
    )
    
    # -- Functions --
    @api.model
    # Updates the 'order_ir_route' of landmarks in a route and 'url_maps' of the route 
    # when a new landmark is added to a route (via landmark_by_route)
    def create(self, vals):
        # Searchs the current maximum order_in_route for this route
        if 'route_id' in vals:
            max_order = self.search(
                [('route_id', '=', vals['route_id'])],
                order='order_in_route desc',
                limit=1
            ).order_in_route or 0
            # Assign the next number (maximum + 1)
            vals['order_in_route'] = max_order + 1
        
        # Updates the url_maps of the route
        rec = super().create(vals)
        if rec.route_id:
            rec.route_id._compute_url_maps()
        return rec
    
    # Updates the 'url_maps' of the route
    # when a landmark is edited (in landmark_by_route)
    def write(self, vals):
        res = super().write(vals)
        for rec in self:
            if rec.route_id:
                rec.route_id._compute_url_maps()
        return res
    
    # Updates the 'order_ir_route' of landmarks in a route and 'url_maps' of the route
    # when a landmark is deleted from a route (via landmark_by_route)
    def unlink(self):
        # Store affected routes before deleting
        routes_to_update = self.mapped('route_id')
        
        # Delete the records
        res = super().unlink()
        
        # Reorder the remaining landmarks on each affected route
        for route in routes_to_update:
            # Get all route landmarks sorted by their current order_in_route
            landmarks_in_route = self.search(
                [('route_id', '=', route.id)],
                order='order_in_route asc'
            )
            
            # Reassign the order_in_route sequentially (1, 2, 3...)
            for index, landmark in enumerate(landmarks_in_route, start=1):
                landmark.write({'order_in_route': index})
            
            # Update the url_maps of the route
            route._compute_url_maps()
        
        return res
    
    @api.depends('route_id', 'landmark_id')
    #Computes if the landmark is a duplicate in a route
    def _compute_is_duplicate(self):
        for record in self:
            # If the record is empty, skip it
            if not record.route_id or not record.landmark_id:
                record.is_duplicate = False
                continue
            
            # Conunting with search_count the number of times that the landmark appears in a route
            same_landmark_count = self.search_count([
                ('route_id', '=', record.route_id.id),
                ('landmark_id', '=', record.landmark_id.id)
            ])
            
            # If the landmark appears more than once, it's duplicated
            record.is_duplicate = (same_landmark_count > 1)