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


author = 'Ferley, Jorge'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'alocations'
    players_per_group = None
    num_rounds = 1
    inv_a = [15, 15, 15, 15, -8, -8, -8, -8]
    inv_b = [-9, -9, -9, -9, 14, 14, 14, 14]
    inv_example = [10, 10, 10, 10, -5, -5, -5, -5]
    inv_labels = ['', '', '', '', '', '', '', '']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
