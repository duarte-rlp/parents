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
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    row_1 = models.IntegerField()
    row_2 = models.IntegerField()
    row_3 = models.IntegerField()
    row_4 = models.IntegerField()
    row_5 = models.IntegerField()
    row_6 = models.IntegerField()
