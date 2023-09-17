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


author = '@hopkeinst'

doc = """
Rentabilidad variable
"""


class Constants(BaseConstants):
    name_in_url = 'choice_2'
    description = 'Actividad 2: Rentabilidad variable'
    players_per_group = None
    num_rounds = 1
    investment_heads = [
                        9000,
                        8100,
                        7200,
                        6300,
                        5400,
                        3600,
                        1800,
                        0
                        ]
    investment_tails = [
                        9000,
                        17100,
                        21600,
                        22500,
                        27000,
                        28800,
                        34200,
                        36000
                        ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    time_choice = models.StringField() # Tiempo total que demora en la pantalla hasta presionar siguiente
    choices = models.StringField() # Cadena con todas las selecciones que tiene antes de presionar siguiente
    # example: el tiempo es en milisegundos
    # { 1: {'investement_heads': 9000, 'investment_tails': 9000, 'time': 4750}, 2: {'investement_heads': 5400, 'investment_tails': 27000, 'time': 9641}}
    
    investment_heads = models.IntegerField() # Guarda la inversion de cara escogida
    investment_tails = models.IntegerField() # Guarda la inversion de sello escogida
    n_investment = models.IntegerField() # Numero de la inversion escogida

    # Para los pagos
    coin_toss = models.StringField() # Lado de la moneda
    payoff_amount_app = models.IntegerField() # Total que se paga por esta app

    name_app_n = models.IntegerField(default = 1)
    name_app = models.StringField(default = 'choice_2')
    name_app_2_user = models.StringField(default = 'Rentabilidad variable')
