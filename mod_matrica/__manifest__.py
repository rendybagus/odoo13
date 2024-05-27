# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Matrica Test',
    'author': 'M Rendy Baguspriawan',
    'category': '',
    'version': '13.0.1.1.0',
    'description': """""",
    'summary': 'Odoo 13',
    'sequence': 10,
    'website': '',
    'depends': [
        'base','crm'
     ],
    'license': 'LGPL-3',
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead.xml',
        'views/segment_product.xml',
    ],
    'qweb': [],
    'application': True,
}
