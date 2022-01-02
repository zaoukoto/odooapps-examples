# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management',
    'version' : '14.0',
    'summary': 'Hospital Management Software',
    'sequence': 1,
    'description': """Hospital Management""",
    'category': 'Productivity',
    'website': 'https://altela.my.id',
    'depends' : [],
# Insert your .xml here
    'data': [
        'views/patient.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
