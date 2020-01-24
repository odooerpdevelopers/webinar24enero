# -*- coding: utf-8 -*-
{
    'name': "Product price 2",

    'summary': """
       Agrega un nuevo campo para precio 2 en el form del producto
       """,

    'description': """
       Agrega un nuevo campo para precio 2 en el form del producto
        
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        "views/product_view.xml",
    ],
}
