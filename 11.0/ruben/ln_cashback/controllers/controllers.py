# -*- coding: utf-8 -*-
from odoo import http

# class LnCashback/(http.Controller):
#     @http.route('/ln_cashback//ln_cashback//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ln_cashback//ln_cashback//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ln_cashback/.listing', {
#             'root': '/ln_cashback//ln_cashback/',
#             'objects': http.request.env['ln_cashback/.ln_cashback/'].search([]),
#         })

#     @http.route('/ln_cashback//ln_cashback//objects/<model("ln_cashback/.ln_cashback/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ln_cashback/.object', {
#             'object': obj
#         })