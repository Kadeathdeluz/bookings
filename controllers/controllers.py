# -*- coding: utf-8 -*-
# from odoo import http


# class Bookings(http.Controller):
#     @http.route('/bookings/bookings/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bookings/bookings/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bookings.listing', {
#             'root': '/bookings/bookings',
#             'objects': http.request.env['bookings.bookings'].search([]),
#         })

#     @http.route('/bookings/bookings/objects/<model("bookings.bookings"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bookings.object', {
#             'object': obj
#         })
