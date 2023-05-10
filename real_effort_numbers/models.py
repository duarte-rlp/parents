import random

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


author = 'Eugene and Charlie'

doc = """
A mental arithmetic task
"""


class Constants(BaseConstants):
    name_in_url = 'real_effort_numbers'
    players_per_group = None
    task_timer = 60
    num_rounds = 1000
    marks_per_correct_answer = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass        

class Player(BasePlayer):
    p1 = models.IntegerField(label='2 x 9')
    p2 = models.IntegerField(label='3 x 20')
    p3 = models.IntegerField(label='4 x 19')
    p4 = models.IntegerField(label='20 - 9')
    p5 = models.IntegerField(label='60 - 19')
    p6 = models.IntegerField(label='18 - 20')
    p7 = models.IntegerField(label='9% de 800')
    p8 = models.IntegerField(label='10% de 800')
    p9 = models.IntegerField(label='19% de 800')
    p110 = models.IntegerField(label='20% de 800')
