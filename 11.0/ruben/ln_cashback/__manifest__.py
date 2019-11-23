# -*- coding: utf-8 -*-
{
    'name': "ln_cashback",

    'summary': """
        Give PoS customers the option to receive change back in satoshis, instead of coins.
        """,

    'description': """
        Give PoS customers the option to receive change back in satoshis, instead of coins.
    """,

    'author': "@21isenough / @watermaniak",
    'website': "https://www.twitter.com/21isenough",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}