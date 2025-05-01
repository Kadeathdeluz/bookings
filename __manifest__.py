# -*- coding: utf-8 -*-
{
    'name': "Reservas",

    'summary': "Permite gestionar las reservas (crear, consultar, modificar).",

    'description': """
         El módulo permite automatizar la reserva de hospedajes para un cliente, para una ruta y con un pack contratado.
        - Dados los datos del cliente, gestiona la reserva de los hospedajes, teniendo en cuenta el tipo de pack elegido y la disponibilidad de los hospedajes.
        - Permite crear reservas asociadas a un cliente, una ruta y un pack.
        - Lista todas las rutas de todos los clientes.
        - Tiene en cuenta también aspectos como que se viaje con animales o con personas con movilidad reducida.
        - En caso de realizar las reservas correctamente, envía una notificación con las reservas realizadas al cliente antes de iniciar la ruta.
    """,

    'author': "Roldán Sanchis Martínez",
    'website': "https://github.com/Kadeathdeluz/remoto_reservas_roldan",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    
    'application': True,

    # always loaded
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/views.xml',
        'views/templates.xml',
        # Data
        # 'data/clients.xml',
        # 'data/items.xml',
        # 'data/landmarks.xml',
        # 'data/packs.xml',
        # 'data/routes.xml',
        # 'data/ladnmarks_by_routes.xml',
        # 'data/lodgins.xml',
        # 'data/journeys.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
