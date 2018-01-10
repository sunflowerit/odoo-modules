# -*- coding: utf-8 -*-
{
    'name': 'Timesheet invoice release',
    'version': '8.0.1.0.0',
    'summary': 'Release timesheet lines after invoice was cancelled',
    'author': 'Sunflower IT',
    'website': 'http://www.sunflowerweb.nl',
    'category': 'Sales Management',
    'depends': [
        'hr_timesheet_invoice'
    ],
    'data': ['account_invoice_view.xml'],
    'installable': True,
}
