# -*- coding: utf-8 -*-
# from odoo import http


# class QrCodeSaleOrder(http.Controller):
#     @http.route('/qr_code_sale_order/qr_code_sale_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qr_code_sale_order/qr_code_sale_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qr_code_sale_order.listing', {
#             'root': '/qr_code_sale_order/qr_code_sale_order',
#             'objects': http.request.env['qr_code_sale_order.qr_code_sale_order'].search([]),
#         })

#     @http.route('/qr_code_sale_order/qr_code_sale_order/objects/<model("qr_code_sale_order.qr_code_sale_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qr_code_sale_order.object', {
#             'object': obj
#         })
