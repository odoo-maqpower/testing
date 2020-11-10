# coding: utf-8
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class AccountMove(models.Model):
	_inherit = 'account.move'

	def post(self):
		# OVERRIDE
		for move in self.filtered(lambda move: move.is_invoice()):
			for line in move.line_ids:
				stock_moves = line.mapped('sale_line_ids.move_ids').filtered(lambda r: r.state == 'done' and not r.scrapped)
				if not stock_moves:
					continue
				landed_costs = self.env['stock.landed.cost'].sudo().search([
					('picking_ids', 'in', stock_moves.mapped('move_orig_fifo_ids.picking_id').ids),
					('l10n_mx_edi_customs_number', '!=', False),
				])
				if not landed_costs:
					continue

				list_date = []
				for lc in landed_costs: list_date.append(str(lc.date))
				join_date = ', '.join(list_date)                

				line.name = line.name + '\n' + join_date
		super(AccountMove, self).post()
