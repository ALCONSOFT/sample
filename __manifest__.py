# -*- coding: utf-8 -*-
{
    'name': "sample",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Strange Matter: Materia Extraña en mestras de Caña de Azúcar
    """,

    'author': "Alconsoft",
    'website': "http://www.alconsoft.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2020-12-09 - 18:00',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','fincas_pma'],

    # always loaded
    'data': [
        'security/sample_security.xml',
        'security/ir.model.access.csv',
        'views/sample_views.xml',
        'views/templates.xml',
        'data/sample_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
