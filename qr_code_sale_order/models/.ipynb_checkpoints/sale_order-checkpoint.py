from odoo import models, fields, api
from odoo.http import request
from .qr_code_base import generate_qr_code


class QRCodeSale(models.Model):
    _inherit = 'sale.order'

    qr_image = fields.Binary("QR Code", compute='_generate_qr_code')
    qr_in_report = fields.Boolean('Show QR in Report')

    def _generate_qr_code(self):
        base_url = request.env['ir.config_parameter'].get_param('web.base.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        self.qr_image = generate_qr_code(base_url)
