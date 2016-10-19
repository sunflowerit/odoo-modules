# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

{
    'sequence': 500,
    "name" : "Sale Order Price Review",
    "version" : "1.2",
    "author" : "Sunflower IT",
    "category": 'Sales Management',
    'complexity': "normal",
    "description": """
Review sale order line prices
=============================

This module allows to defer setting price for a sales order line to directly before invoicing.
So after confirmation.
To use this feature, you need to set a sale order to the "Review prices" state.
In that state, the prices can be edited.
Also, any printout of the sales order in that state will not contain any pricing, so can be sent
to customer without problems.

    """,
    'website': 'http://sunflowerweb.nl',
    "depends" : ["sale"],
    'init_xml': [],
    'data': [
        'sale_view.xml',
        'sale_workflow.xml',
        'sale_report.xml'
    ],
    'demo_xml': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
