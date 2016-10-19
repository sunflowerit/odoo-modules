# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2012-2012 ChriCar Beteiligungs- und Beratungs- GmbH (<http://www.camptocamp.at>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
 
from openerp import models, fields, _
from openerp.exceptions import Warning

class sale_order(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('reprice', 'Review pricing')])
    order_line_reprice = fields.One2many('sale.order.line', 'order_id', 'Order Lines', readonly=True, states={'draft': [('readonly', False)], 'reprice': [('readonly', False)], 'sent': [('readonly', False)]}, copy=True)

    def allow_reprice(self, cr, uid, ids, context=None):
        for order in self.browse(cr, uid, ids, context):
            if order.invoice_ids:
                raise Warning(_('You cannot edit prices for this Sale Order, because invoice %s has been generated.') % (inv.name,))
        return True

    def action_reprice(self):
        """ Makes prices editable. """
        self.state = 'reprice'
        for line in self.order_line:
            line.state = 'draft'

    def action_repriced(self):
        """ Confirm prices. """
        self.state = 'manual'
        for line in self.order_line:
            line.state = 'confirmed'


class sale_order_line(models.Model):
    _inherit = 'sale.order.line'

    price_tbd = fields.Boolean('TBD')


