from os import environ
import os

SESSION_CONFIGS = [
    {
        'name': 'test',
        'display_name': 'Test General',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'real_effort_numbers', 'checker1', 'choice_2', 'training', 'allocations', 'real', 'choice', 'survey', 'final'],
    },
    {
        'name': 'home',
        'display_name': 'Instrucciones Generales',
        'num_demo_participants': 1, 
        'app_sequence': ['home'],
    },
    {
        'name': 'math_operations',
        'display_name': 'Preguntas iniciales',
        'num_demo_participants': 1, 
        'app_sequence': ['real_effort_numbers'],
    },
    {
        'name': 'choice_2',
        'display_name': 'Actividad 1: Rentabilidad variable',
        'num_demo_participants': 1, 
        'app_sequence': ['choice_2'],
    },
    {
        'name': 'checker1',
        'display_name': 'Pregunta',
        'num_demo_participants': 1, 
        'app_sequence': ['checker1'],
    },
    {
        'name': 'graphs',
        'display_name': 'Actividad 2: Instrucciones',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'training'],
    },
    {
        'name': 'problems',
        'display_name': 'Actividad 2: Decisiones de Inversión',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'allocations'],
    },
    {
        'name': 'real',
        'display_name': 'Actividad 3: Cultivos',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'real'],
    },
    {
        'name': 'choice',
        'display_name': 'Actividad 4: Invertir o No invertir',
        'num_demo_participants': 1, 
        'app_sequence': ['choice'],
    },
    {
        'name': 'payoff_choice',
        'display_name': 'Votación Grupal',
        'num_demo_participants': 1, 
        'app_sequence': ['payoff_choice'],
    },
    {
        'name': 'survey',
        'display_name': 'Encuesta',
        'num_demo_participants': 1, 
        'app_sequence': ['survey'],
    },
    {
        'name': 'final',
        'display_name': 'Cálculo de pagos',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'choice_2', 'allocations', 'real', 'choice', 'final'],
    },
]

ROOMS = [
    dict(
        name='PC',
        display_name='PC',
        participant_label_file='_rooms/PC.txt',
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, 
    participation_fee=0.00, 
    doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'COP'
USE_POINTS = False

ADMIN_USERNAME = 'rafael'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ 
Hola
"""

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

PARTICIPANT_FIELDS = ['graphType']

DEBUG=True

SECRET_KEY = 'ych58g9m8ay^q)l^*n^!=8!t#tjo%$-kb53wkh96i$es(yp7b+'

OTREE_STATIC_ROOT = os.environ.get("OTREE_STATIC_ROOT", "/app/static_files")

## Variables para Heroku
"""
OTREE_ENV = os.environ.get("OTREE_ENV", "production")
OTREE_SECRET_KEY = os.environ.get("OTREE_SECRET_KEY")
SECRET_KEY = os.environ.get("OTREE_SECRET_KEY")
OTREE_DATABASE_URL = os.environ.get("DATABASE_URL")

"""
