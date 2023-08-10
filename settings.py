from os import environ

SESSION_CONFIGS = [
    {
        'name': 'test',
        'display_name': 'Test General',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'real_effort_numbers', 'icl', 'choice_2', 'checker1', 'training', 'allocations', 'icl2','choice', 'real', 'survey', 'final'],
    },
    {
        'name': 'home',
        'display_name': 'Home: instrucciones',
        'num_demo_participants': 1, 
        'app_sequence': ['home'],
    },
    {
        'name': 'math_operations',
        'display_name': 'Preguntas iniciales: real_effort_numbers',
        'num_demo_participants': 1, 
        'app_sequence': ['real_effort_numbers'],
    },
    {
        'name': 'icl',
        'display_name': 'Actividad 1: Rentabilidad fija o variable - ICL 1',
        'num_demo_participants': 1, 
        'app_sequence': ['icl'],
    },
    {
        'name': 'choice_2',
        'display_name': 'Actividad 2: Rentabilidad variable - choice_2',
        'num_demo_participants': 1, 
        'app_sequence': ['choice_2'],
    },
    {
        'name': 'checker1',
        'display_name': 'Pregunta: checker1',
        'num_demo_participants': 1, 
        'app_sequence': ['checker1'],
    },
    {
        'name': 'graphs',
        'display_name': 'Instrucciones de Inversión: Training graphs - training',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'training'],
    },
    {
        'name': 'problems',
        'display_name': 'Parte 3: Allocation problems - allocations',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'allocations'],
    },
    {
        'name': 'real',
        'display_name': 'Parte 5: Real assets - real',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'real'],
    },
    {
        'name': 'choice',
        'display_name': 'Actividad 6: Invertir o no invertir - choice',
        'num_demo_participants': 1, 
        'app_sequence': ['choice'],
    },
    {
        'name': 'couple',
        'display_name': '¿Continua solo o en parejas?',
        'num_demo_participants': 1, 
        'app_sequence': ['couple'],
    },
    {
        'name': 'final',
        'display_name': 'Test Payoffs: Choice_2, ICL1, Choice',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'icl', 'icl2', 'choice', 'final'],
    },
    # {
    #     'name': 'icl2',
    #     'display_name': 'ICL 2',
    #     'num_demo_participants': 1, 
    #     'app_sequence': ['home', 'icl2'],
    # },
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

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'ych58g9m8ay^q)l^*n^!=8!t#tjo%$-kb53wkh96i$es(yp7b+'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

PARTICIPANT_FIELDS = ['graphType']

DEBUG=True

