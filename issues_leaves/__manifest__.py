# -*- coding: utf-8 -*-
{
    'name': "Leave Issues",

    'summary': """
        Adecuaciones en el modulo de Ausencias""",

    'description': """
        Filtro por dias no vencidos, mostrar dias restates en solicitud de ausencia y filtro por departamento de la persona actual
    """,
    'author': "GTVP",
    'website': "http://www.gtvp.odoo.com",
    'category': 'GTVP',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_holidays'],

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