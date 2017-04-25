# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from itertools import groupby
import time
from datetime import datetime as dt

from openerp import fields, models, api, _
import openerp.addons.decimal_precision as dp


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def _get_report_analytic_lines(self):
        for invoice in self:
            lines = self.env['hr.analytic.timesheet'].search([
                ('invoice_id', '=', invoice.id)
            ])
            invoice.report_analytic_lines = lines

    report_analytic_lines = fields.One2many('hr.analytic.timesheet',
        string='Analytic lines',
        help="The analytic lines coupled to this invoice.",
        compute='_get_report_analytic_lines')

    @api.multi
    def lines_per_project(self):
        """ Return analytic lines per project """

        # inspired by odoo/addons/sale_layout/models/sale_layout.py
        def grouplines(ordered_lines, sortkey):
            """ Return lines grouped by category """
            grouped_lines = []
            for key, valuesiter in groupby(ordered_lines, sortkey):
                group = {}
                group['category'] = key
                group['lines'] = list(v for v in valuesiter)
                grouped_lines.append(group)
            return grouped_lines

        sortkey = lambda x: x.issue_id or ''
        lines = self.report_analytic_lines
        ordered_lines = sorted(lines, key=sortkey)
        grouped = grouplines(ordered_lines, sortkey)

        for group in grouped:
            # Get the issue name and description from the issue
            so_obj = self.env['project.issue']
            if group['category']:
                # so_rec = so_obj.search([('id', '=', group['category'].id)])
                so_rec = so_obj.search([('id', '=', group['category'].id)])
                so_rec = so_rec[0] if len(so_rec) else False
            else:
                so_rec = False
            group['issue'] = so_rec and so_rec.name or ''
            group['description'] = so_rec and so_rec.description or ''
            stage = so_rec and so_rec.stage_id
            # the_date = so_rec and so_rec.date_deadline or None
            # keep this for when we will have to use strptime to reprocess the 'thedate' string
            # group['delivery_date'] = time.strftime("%d %b %Y", the_date) if the_date else 'In afwachting'
            group['stage_id'] = stage if stage else ''

        return grouped
