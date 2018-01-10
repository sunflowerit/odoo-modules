# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import  models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def release_timesheet_lines(self):
        self.ensure_one()
        self.env['hr.analytic.timesheet'].search([
            ('invoice_id', '=', self.id)
        ]).with_context(override_check=True).write({'invoice_id': None})
