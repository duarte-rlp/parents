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
    name_in_url = 'checker1'
    players_per_group = None
    num_rounds = 1
    colors_checker = ['Branco', 'Turquesa', 'Vermelho', 'Preto']
    correct_color = "Turquesa"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #cnt_mistakes = models.IntegerField()
    #mistakes_checker = models.StringField()
    answer_checker = models.StringField()
    time_checker = models.StringField()
