# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Asset Management',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Strativ Asset Management System',
    'depends': ['web'],
    'sequence': 1,
    'data': [
        'security/ir.model.access.csv',
        'views/assets_views.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}