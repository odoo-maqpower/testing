# coding: utf-8
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class AccountMove(models.Model):
	_inherit = 'account.move'

    #origin_warehouse_id = 