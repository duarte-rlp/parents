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
            1018,
            1300,
            1710,
            1800,
            2044,
            1826,
            1662,
            1448
            ]
    cultivo_2 = [
            1728,
            1648,
            1366,
            766,
            1036,
            1646,
            1768,
            1642
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
    time_cultivos = models.StringField() # tiempo que demoró llenando correctamente las respuestas
    cnt_mistakes = models.IntegerField() # cantidad de errores al llenar los recuadros
