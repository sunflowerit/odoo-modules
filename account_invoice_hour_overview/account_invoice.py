# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from itertools import groupby
import time
from datetime import datetime as dt

from openerp import fields, models, api, _
import openerp.addons.decimal_precision as dp
import itertools
import pprint
pp = pprint.PrettyPrinter(indent=4)

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    report_analytic_lines = fields.One2many(comodel_name="hr.analytic.timesheet",
        inverse_name="invoice_id", string="Analytic lines",
        help="The analytic lines coupled to this invoice.")

    @api.multi
    def lines_per_project(self):
        """ Return analytic lines per project """

        def grouplines(self, field='issue_id'):
            for key, group in itertools.groupby(
                    self.sorted(lambda record: record[field]),
                    lambda record: record[field]
            ):
                yield key, sum(group, self.browse([]))

        lines = self.report_analytic_lines
        grouped = []
        for category, lines in grouplines(lines, 'issue_id'):
            group = {}
            group['category'] = category
            group['lines'] = list(lines)
            grouped.append(group)

        for group in grouped:
            # Get the issue name and description from the issue
            issue_obj = self.env['project.issue']
            if group['category']:
                issue_rec = issue_obj.search([('id', '=', group['category'].id)])
                issue_rec = issue_rec[0] if len(issue_rec) else False
            else:
                issue_rec = False
            group['issue'] = issue_rec and issue_rec.name or ''
            group['description'] = issue_rec and issue_rec.description or ''
            stage = issue_rec and issue_rec.stage_id
            # the_date = issue_rec and issue_rec.date_deadline or None
            # keep this for when we will have to use strptime to reprocess the 'the_date' string
            # group['delivery_date'] = time.strftime("%d %b %Y", the_date) if the_date else 'In afwachting'
            group['stage_id'] = stage if stage else ''

        return grouped
