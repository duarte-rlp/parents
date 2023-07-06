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
                41,
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

    p5 = models.IntegerField()
    p5_cnt_mistakes = models.IntegerField()
    p5_mistakes = models.StringField()
    p5_time = models.StringField()

    p6 = models.IntegerField()
    p6_cnt_mistakes = models.IntegerField()
    p6_mistakes = models.StringField()
    p6_time = models.StringField()

    p7 = models.IntegerField()
    p7_cnt_mistakes = models.IntegerField()
    p7_mistakes = models.StringField()
    p7_time = models.StringField()

    p8 = models.IntegerField()
    p8_cnt_mistakes = models.IntegerField()
    p8_mistakes = models.StringField()
    p8_time = models.StringField()

    p9 = models.IntegerField()
    p9_cnt_mistakes = models.IntegerField()
    p9_mistakes = models.StringField()
    p9_time = models.StringField()

    p10 = models.IntegerField()
    p10_cnt_mistakes = models.IntegerField()
    p10_mistakes = models.StringField()
    p10_time = models.StringField()
    
    cnt_question = models.IntegerField(initial = 1)
