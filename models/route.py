# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Route(models.Model):
    """
    Model that represents a route of the Camino de Santiago.
    """
    _name = 'bookings.route'
    _description = 'Represents a route of the Camino de Santiago'

    # -- Table fields --
    name = fields.Char(string='Name', required=True)
    distance = fields.Float(string="Distance") # Not real distance
    url_maps = fields.Char()
    description = fields.Text()

    # -- Calculated fields --
    is_circular = fields.Boolean(
        string="Circular Route",
        compute='_compute_is_circular',
        store=True,
        help="Indicates if the route starts and ends at the same landmark"
    )

    circular_emoji = fields.Char(
        string="Type",
        compute= '_compute_circular_emoji',
        
    )

    # -- Relations --
    # Related landmarks to the current route
    related_landmarks_ids = fields.One2many('bookings.landmark_by_route', 'route_id', string=" Landmarks")

    # Related lodgins to the current route
    related_lodgins_ids = fields.Many2many(
        comodel_name='bookings.lodgin',
        relation='bookings_lodgin_by_route',
        column1='route_id',
        column2='lodgin_id',
        string='Lodgins'
    )
    
    # -- Functions --
    # Returns the name of the Route
    def name_get(self):
        return [(rec.id, rec.name) for rec in self]
    
    # Builds the url_maps attribute based on the related landmarks of the route
    def _compute_url_maps(self):
        base_url = "https://www.google.com/maps/dir"
        
        # Goes through the routes
        for route in self:
            # sorted landmarks by order in route
            sorted_landmarks = sorted(
                route.related_landmarks_ids,
                # Lambda function to return sorted landmarks (by order_in_route)
                key=lambda x: x.order_in_route # key to sort landmarks (by order_in_route)
            )
            # empty list to store coords to create the url
            coords = []
            for entry in sorted_landmarks:
                landmark = entry.landmark_id
                if landmark and landmark.point_x and landmark.point_y:
                    # adds coords to the list
                    coords.append(f"{landmark.point_y},{landmark.point_x}") # First append Latitude, then Longitude
            if coords:
                zoom = f"/@{coords[0]},15z" # Zoom points to the firs coord of the route with a 15z zoom
                route.url_maps = f"{base_url}/{'/'.join(coords)}{zoom}"
            else:
                route.url_maps = False
    
    # Computes the emoji associated to the circular status (True -> '🔄', False -> '➡️')
    @api.depends('is_circular')
    def _compute_circular_emoji(self):
        for route in self:
            route.circular_emoji = "Circular route 🔄" if route.is_circular else "Lineal route ➡️" # It can be only the emoji

    @api.depends('related_landmarks_ids')
    # Computes if the route is circular or not
    def _compute_is_circular(self):
        for route in self:
            if not route.related_landmarks_ids:
                route.is_circular = False
                continue # Skips the current route
            
            # Sorts landmarks by order in route
            sorted_landmarks = sorted(
                route.related_landmarks_ids,
                key=lambda x: x.order_in_route
            )
            
            # Gets the first and last landmark
            first_landmark = sorted_landmarks[0].landmark_id
            last_landmark = sorted_landmarks[-1].landmark_id
            
            # Assigns the comparison to the is_circular field
            route.is_circular = (first_landmark == last_landmark)