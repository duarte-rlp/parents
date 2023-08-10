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
                        15000,
                        13500,
                        12000,
                        10500,
                        9000,
                        6000,
                        3000,
                        0
                        ]
    investment_tails = [
                        15000,
                        28500,
                        36000,
                        37500,
                        45000,
                        48000,
                        57000,
                        60000
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
    
    investment_heads = models.IntegerField() # Inversion de cara escogida
    investment_tails = models.IntegerField() # Inversion de sello escogida
    n_investment = models.IntegerField() # Numero de la inversion escogida

    coin_toss = models.StringField() # Lado de la moneda
    payoff_amount_app = models.IntegerField() # Total que se paga por esta app
