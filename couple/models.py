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
Elegir si pago va a ser solo o en pareja
"""


class Constants(BaseConstants):
    name_in_url = 'couple'
    description = '¿Continua solo o en parejas?'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_choice = models.StringField() # Tiempo total que demora en la pantalla hasta presionar siguiente
    choices = models.StringField() # Cadena con todas las selecciones que tiene antes de presionar siguiente

    option = models.StringField()


