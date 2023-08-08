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
    n_questions = ['ocho', 8]
    players_per_group = None
    task_timer = 60
    num_rounds = 1
    marks_per_correct_answer = 1
    questions = [
                'Cuál sería el resultado de 6 x 19',
                'Cuánto sería el 9% de 200',
                'Cuál sería el resultado de 18 - 20',
                'Cuál sería el resultado de 60 - 19',
                'Suponga que usted posee $ 100.000 en un producto financiero que paga un interés anual del 2%. Si se mantiene por 5 años dicho producto, sin realizar ningún otro pago ni retirar el dinero, ¿cuánto tendrá al terminar de estos 5 años?',
                'Suponga que usted posee $ 100.000 en un producto financiero que paga un interés de un 1% anual. Usted sabe que la tasa de inflación es de un 2% anual. Después de un año usted podrá comprar:',
                'La siguiente frase es verdadera o falsa: «Las acciones son normalmente más riesgosas que los bonos o títulos»',
                'La siguiente frase es verdadera o falsa: «Comprar una acción de una empresa es menos riesgoso que comprar con el mismo dinero varias acciones de distintas empresas»'
                ]
    answers =   [
                '114',
                '18',
                '-2',
                '41',
                '> 102.000',  # Más de 102.000
                '< 100.000',  # Menos de 100.000
                'true',
                'false'
                ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass        

class Player(BasePlayer):
    p1 = models.StringField()
    p1_cnt_mistakes = models.IntegerField()
    p1_mistakes = models.StringField()
    p1_time = models.StringField()

    p2 = models.StringField()
    p2_cnt_mistakes = models.IntegerField()
    p2_mistakes = models.StringField()
    p2_time = models.StringField()

    p3 = models.StringField()
    p3_cnt_mistakes = models.IntegerField()
    p3_mistakes = models.StringField()
    p3_time = models.StringField()

    p4 = models.StringField()
    p4_cnt_mistakes = models.IntegerField()
    p4_mistakes = models.StringField()
    p4_time = models.StringField()

    p5 = models.StringField()
    p5_cnt_mistakes = models.IntegerField()
    p5_mistakes = models.StringField()
    p5_time = models.StringField()

    p6 = models.StringField()
    p6_cnt_mistakes = models.IntegerField()
    p6_mistakes = models.StringField()
    p6_time = models.StringField()

    p7 = models.StringField()
    p7_cnt_mistakes = models.IntegerField()
    p7_mistakes = models.StringField()
    p7_time = models.StringField()

    p8 = models.StringField()
    p8_cnt_mistakes = models.IntegerField()
    p8_mistakes = models.StringField()
    p8_time = models.StringField()
    
    cnt_question = models.IntegerField(initial = 1)
