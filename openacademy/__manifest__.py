{
    'name': "Open Academy",
    'summary': """Manage trainings""",
    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Test',
    'version': '0.1',
    'depends': ['base', 'board'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/partner.xml',
        'report/session_board.xml',
        'views/reports.xml',
        'wizard/wizard.xml',
    ],
    'demo': [
        'demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
