# -*- coding: utf-8 -*-

{
    'name': 'Testserver',
    'version': '0.1',
    'summary': 'Testserver',
    'description': """
Mark this server as a testserver!
=================================
So that it is not confused with the real one
    """,
    'author': 'Sunflower IT',
    'website': 'http://sunflowerweb.nl',
    'category': 'Specific Industry Applications',
    'sequence': 0,
    'depends': ['base', 'web'],
    'data': [
        'testserver.xml',
    ],
    'installable': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
