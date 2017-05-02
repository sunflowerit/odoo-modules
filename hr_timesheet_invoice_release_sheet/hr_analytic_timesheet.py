# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, api, _
from openerp.exceptions import Warning as UserError


class HrAnalyticTimesheet(models.Model):
    _inherit = "hr.analytic.timesheet"

    @api.multi
    def write(self, vals):
        self._check_with_context()
        return super(HrAnalyticTimesheet, self).write(vals)

    @api.multi
    def unlink(self):
        self._check_with_context()
        return super(HrAnalyticTimesheet, self).unlink()

    def _check(self, cr, uid, ids):
        """ Disable this check """
        return True

    @api.multi
    def _check_with_context(self):
        """ Replace with a check that properly listens to context """
        if self.env.context.get('override_check', None):
            return True
        for att in self:
            if att.sheet_id and att.sheet_id.state not in ('draft', 'new'):
                raise UserError(_('Error!'), _('You cannot modify an entry in a confirmed timesheet.'))
        return True


