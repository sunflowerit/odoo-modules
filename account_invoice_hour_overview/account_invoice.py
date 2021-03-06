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
    hour_summary_invoice = fields.Boolean(string="Summary of Hours?", default=False)
    personal_info = fields.Boolean(string="Include Personal Info?", default=False)

    @api.multi
    def lines_per_project(self):
        """ Return analytic lines per project """

        def grouplines(self, field='issue_id'):
            for key, group in itertools.groupby(
                    self.sorted(lambda record: record[field].id),
                    lambda record: record[field]
            ):
                yield key, sum(group, self.browse([]))

        analytic_lines = self.report_analytic_lines

        for issue, lines in grouplines(analytic_lines, 'issue_id'):
            yield {'category': issue, 'lines': lines}
