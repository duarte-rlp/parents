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
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'choice'
    description = 'Atividade 4: Lançar ou não lançar uma moeda'
    players_per_group = None
    num_rounds = 1
    loss = [
            -6,
            -9,
            -12,
            -15,
            -18,
            -21
    ]
    earnings = [
                18,
                18,
                18,
                18,
                18,
                18
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

    # Para los pagos
    n_investment = models.IntegerField() # Saber al final cual es la fila que se escoge
    coin_toss = models.StringField() # Lado de la moneda
    payoff_amount_app = models.IntegerField() # Total que se paga por esta app

    name_app_n = models.IntegerField(default = 4)
    name_app = models.StringField(default = 'choice')
    name_app_2_user = models.StringField(default = 'Lançar ou não as moedas')
