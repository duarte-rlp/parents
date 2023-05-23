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
    num_rounds = 1
    marks_per_correct_answer = 1
    questions = [
                '2 x 10',
                '3 x 20',
                '6 x 19',
                '20 - 9',
                '60 - 19',
                '18 - 20',
                '10% de 100',
                '10% de 800',
                '20% de 200',
                '9% de 200'    
                ]
    answers =   [
                20,
                60,
                114,
                11,
                51,
                -2,
                10,
                80,
                40,
                18
                ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass        

class Player(BasePlayer):
    p1 = models.IntegerField()
    p2 = models.IntegerField()
    p3 = models.IntegerField()
    p4 = models.IntegerField()
    p5 = models.IntegerField()
    p6 = models.IntegerField()
    p7 = models.IntegerField()
    p8 = models.IntegerField()
    p9 = models.IntegerField()
    p10 = models.IntegerField()
    cnt_question = models.IntegerField(initial = 1)
