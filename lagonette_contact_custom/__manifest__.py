# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'La Gonnette contact custom',
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'description': "La Gonnette : custom fields and views for partners",
    'depends': ['base','membership'],
    'data': [
        'views/res_partner_view.xml'
],
    'license': 'LGPL-3',
    'installable': True,
    "auto_install": False,
    "application": False,
}
