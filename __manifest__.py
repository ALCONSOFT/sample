# -*- coding: utf-8 -*-
{
    'name': "sample",

    'summary': """
        Strange Matter: Materia Extraña en mestras de Caña de Azúcar""",

    'description': """
        Strange Matter: Materia Extraña en mestras de Caña de Azúcar
    """,

    'author': "Alconsoft",
    'website': "http://www.alconsoft.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': 'Rama main 2020-12-26 - 12:25',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','fincas_pma'],

    # always loaded
    'data': [
        'security/sample_security.xml',
        'security/ir.model.access.csv',
        'views/sample_views.xml',
        'views/templates.xml',
        'data/sample_data.xml',
        'static/xls/product.template.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
