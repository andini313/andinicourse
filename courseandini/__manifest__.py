# -*- coding: utf-8 -*-
{
    'name': "courseandini",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/daftarcourse_view.xml',
        'views/kelompokcourse_view.xml',
        'views/mentor_view.xml',
        'views/siswa_view.xml',
        'views/penjualan_view.xml',
        'report/report.xml',
        'report/print_faktur_penjualan_view.xml',
        'wizard/tambahdaftarcourse_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
