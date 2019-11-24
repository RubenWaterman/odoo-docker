# -*- coding: utf-8 -*-
import random
import requests
import json

from odoo import models, fields, api


class LnCashback(models.Model):
    _name = "ln.cashback"
    _description = (
        "A LN cashback receipt, belonging to a receipt generated in the POS application"
    )

    ln_url = fields.Char("LN URL")
    satoshis = fields.Integer("Change in Satoshi")
    fiat_change = fields.Float("Change in Fiat")
    pos_statement_id = fields.Many2one(
        "pos.order", string="POS statement", ondelete="cascade"
    )
    ln_status = fields.Selection(
        [
            ("PENDING", "Pending LN Payment"),
            ("CLAIMED", "Claimed LN Payment"),
            ("EXPIRED", "Expired LN Payment"),
            ("CANCELLED", "Cancelled LN Payment"),
        ],
        help="""
* Pending LN Payment -- LNURL that still needs to be claimed by customer
* Claimed LN Payment -- LNURL claimed by customer
* Expired LN Payment -- Customer did not claim LNURL
* Cancelled LN Payment -- We cancelled the LNURL
    """,
    )

    # exchange_rate = fields.Float(compute="_fx_rate")
    exchange_rate = fields.Float()

    randomnum = fields.Char(compute="_compute_rand")

    @api.multi
    def _compute_rand(self):
        for item in self:
            if not item.randomnum:
                item.randomnum = str(random.randint(1, 1e6))
        return True

    @api.multi
    def add_sats(self):
        for item in self:
            item.satoshis = 5000
        return True

    @api.multi
    def fx_rate(self):
        for item in self:
            price_request = requests.get(
                "https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCEUR"
            )
            price_json = json.loads(price_request.text)
            item.exchange_rate = price_json["last"]
        return True


# class ln_cashback2(models.Model):
#     _name = 'ln_cashback2.ln_cashback2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
