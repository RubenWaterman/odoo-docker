# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LnCashback(models.Model):
    _name = "ln.cashback"
    _description = (
        "A LN cashback receipt, belonging to a receipt generated in the POS application"
    )

    ln_url = fields.Char("LN URL")
    satoshis = fields.Integer("Amount of Satoshis")
    pos_statement_id = fields.Many2one(
        "pos.order", string="POS statement", ondelete="cascade"
    )

    @api.multi
    def add_sats(self):
        for item in self:
            item.satoshis = 5000
        return True


# class ln_cashback(models.Model):
#     _name = 'ln_cashback.ln_cashback'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
