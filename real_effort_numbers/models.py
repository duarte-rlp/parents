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
                '6 x 19',
                '9% de 200',
                '60 - 19',
                '18 - 20'  
                ]
    answers =   [
                114,
                18,
                41,
                -2
                ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass        

class Player(BasePlayer):
    p1 = models.IntegerField()
    p1_cnt_mistakes = models.IntegerField()
    p1_mistakes = models.StringField()
    p1_time = models.StringField()

    p2 = models.IntegerField()
    p2_cnt_mistakes = models.IntegerField()
    p2_mistakes = models.StringField()
    p2_time = models.StringField()

    p3 = models.IntegerField()
    p3_cnt_mistakes = models.IntegerField()
    p3_mistakes = models.StringField()
    p3_time = models.StringField()

    p4 = models.IntegerField()
    p4_cnt_mistakes = models.IntegerField()
    p4_mistakes = models.StringField()
    p4_time = models.StringField()
        
    cnt_question = models.IntegerField(initial = 1)
