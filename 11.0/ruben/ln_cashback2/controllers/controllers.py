# -*- coding: utf-8 -*-
from odoo import http

# class LnCashback(http.Controller):
#     @http.route('/ln_cashback2/ln_cashback2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ln_cashback2/ln_cashback2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ln_cashback2.listing', {
#             'root': '/ln_cashback2/ln_cashback2',
#             'objects': http.request.env['ln_cashback2.ln_cashback2'].search([]),
#         })

#     @http.route('/ln_cashback2/ln_cashback2/objects/<model("ln_cashback2.ln_cashback2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ln_cashback2.object', {
#             'object': obj
#         })