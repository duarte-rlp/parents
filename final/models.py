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
    name_in_url = 'final'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    activity_pay = models.StringField()
    pago_minimo = models.IntegerField(default = 10000)
    pago_base = models.IntegerField(default = 20000)
    is_menor_pago = models.IntegerField(default = 0) # Si el valor calculado es menor al minimo
    pago_calculo = models.IntegerField()
    pago_real = models.IntegerField()

    data_html = models.StringField()
