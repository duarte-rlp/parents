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
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013,
            2014,
            2015,
            2016,
            2017,
            2018,
            2019,
            2020
            ]
    banano = [
            9.09,
            9.17,
            10.09,
            8.81,
            10.49,
            9.85,
            9.8,
            10.23,
            9.66,
            10.62,
            10.63,
            24.88,
            24.85,
            24.46
            ]
    canha = [
            11.401,
            12.182,
            12.23,
            11.758,
            12.244,
            10.044,
            11.073,
            12.214,
            11.984,
            19.982,
            13.315,
            14.13,
            1.282,
            0.931
            ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    return_banano = models.IntegerField()
