# -*- coding: utf-8 -*-
{
    "name": "ln_cashback2",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    "description": """
        Long description of module's purpose
    """,
    "author": "@21isenough",
    "website": "https://www.twitter.com/21isenough",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base","point_of_sale"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
        "views/ln_cashback2_menu.xml",
        "views/ln_cashback2_edit_menu.xml",
        "views/edit_view.xml",
    ],
    # only loaded in demonstration mode
    "demo": ["demo/demo.xml",],
}
