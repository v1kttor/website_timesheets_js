# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteTimesheetsJs(http.Controller):
#     @http.route('/website_timesheets_js/website_timesheets_js/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_timesheets_js/website_timesheets_js/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_timesheets_js.listing', {
#             'root': '/website_timesheets_js/website_timesheets_js',
#             'objects': http.request.env['website_timesheets_js.website_timesheets_js'].search([]),
#         })

#     @http.route('/website_timesheets_js/website_timesheets_js/objects/<model("website_timesheets_js.website_timesheets_js"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_timesheets_js.object', {
#             'object': obj
#         })