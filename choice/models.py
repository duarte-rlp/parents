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
    name_in_url = 'choice'
    description = 'Actividad 6: Invertir o no invertir'
    players_per_group = None
    num_rounds = 1
    loss = [
            -6000,
            -9000,
            -12000,
            -16000,
            -18000,
            -20000
    ]
    earnings = [
                18000,
                18000,
                18000,
                18000,
                18000,
                18000
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 0 -> No invertir | 1 -> Invertir
    row_1 = models.IntegerField()
    row_2 = models.IntegerField()
    row_3 = models.IntegerField()
    row_4 = models.IntegerField()
    row_5 = models.IntegerField()
    row_6 = models.IntegerField()

    time_choice = models.StringField()

    n_investment = models.IntegerField() # Saber al final cual es la fila que se escoge
    coin_toss = models.StringField() # Lado de la moneda
    payoff_amount_app = models.IntegerField() # Total que se paga por esta app
