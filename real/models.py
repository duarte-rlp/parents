from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'real'
    players_per_group = None
    num_rounds = 1

    anhos = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8
            ]
    cultivo_1 = [
            1.018,
            1.300,
            1.710,
            1.800,
            2.044,
            1.826,
            1.662,
            1.448
            ]
    cultivo_2 = [
            1.728,
            1.648,
            1.366,
            0.766,
            1.036,
            1.646,
            1.768,
            1.642
            ]
    time_steps = 500 # tiempo en aparecer cada punto
    investment_max = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    has_cultivo_1 = models.IntegerField() # cantidad de hectáreas para el cultivo 1
    has_cultivo_2 = models.IntegerField() # cantidad de hectáreas para el cultivo 2
    time_cultivos_1 = models.StringField() # tiempo que demoró con los botones
    time_cultivos_2 = models.StringField() # tiempo que demoró con lel slier
    time_cultivos_3 = models.StringField() # tiempo que demoró con las cajas de introducir cantidad de hectáreas
    cnt_mistakes = models.IntegerField() # cantidad de errores al llenar los recuadros

    # questions page
    #time_cultivos_4 = models.StringField() # tiempo que demoró en responder las 5 preguntas
    #question_1_real = models.StringField()
    #question_2_real = models.StringField()
    #question_3_real = models.StringField()
    #question_4_real = models.StringField()
    #question_5_real = models.StringField()

    # Variables para los pagos
    n_scene = models.IntegerField() # Saber cual escenario se escoge
    amount_cultivo_1 = models.IntegerField() # El total calculado para el cultivo A
    amount_cultivo_2 = models.IntegerField() # El total calculado para el cultivo B
    payoff_amount_app = models.IntegerField() # Total que se paga por esta app

    name_app_n = models.IntegerField(default = 3)
    name_app = models.StringField(default = 'real')
    name_app_2_user = models.StringField(default = 'Cultivos')

