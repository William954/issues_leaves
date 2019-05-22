# -*- coding: utf-8 -*-
from odoo import http

# class IssuesLeaves(http.Controller):
#     @http.route('/issues_leaves/issues_leaves/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/issues_leaves/issues_leaves/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('issues_leaves.listing', {
#             'root': '/issues_leaves/issues_leaves',
#             'objects': http.request.env['issues_leaves.issues_leaves'].search([]),
#         })

#     @http.route('/issues_leaves/issues_leaves/objects/<model("issues_leaves.issues_leaves"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('issues_leaves.object', {
#             'object': obj
#         })