from os import environ

SESSION_CONFIGS = [
    {
        'name': 'test',
        'display_name': 'test',
        'num_demo_participants': 1, 
        'app_sequence': ['survey'],
    },
    {
        'name': 'math_operations',
        'display_name': 'Parte 1: Math',
        'num_demo_participants': 1, 
        'app_sequence': ['real_effort_numbers'],
    },
    {
        'name': 'graphs',
        'display_name': 'Parte 2: Training graphs',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'training'],
    },
    {
        'name': 'problems',
        'display_name': 'Parte 3: Allocation problems',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'allocations'],
    },
    {
        'name': 'choice',
        'display_name': 'Parte 4: Choice - Loss averssion',
        'num_demo_participants': 1, 
        'app_sequence': ['choice'],
    },
    {
        'name': 'real',
        'display_name': 'Parte 5: Real assets',
        'num_demo_participants': 1, 
        'app_sequence': ['home', 'real'],
    },
    {
        'name': 'icl',
        'display_name': 'icl',
        'num_demo_participants': 1, 
        'app_sequence': ['home','icl'],
    },
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

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'ych58g9m8ay^q)l^*n^!=8!t#tjo%$-kb53wkh96i$es(yp7b+'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

PARTICIPANT_FIELDS = ['graphType']
