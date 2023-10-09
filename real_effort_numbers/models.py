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


author = '@hopkeinst'

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
                '¿Cuál sería el resultado de 18 - 20?',
                '¿Cuál sería el resultado de 60 - 19?',
                '¿Cuál sería el resultado de 6 x 19?',
                '¿Cuánto sería el 9% de 200?',
                'Suponga que usted posee $ 100.000 en un producto financiero que paga un interés anual del 2%. Si se mantiene por 5 años dicho producto, sin realizar ningún otro pago ni retirar el dinero, ¿Cuánto tendrá al terminar de estos 5 años?',
                'Suponga que su cuenta de ahorro paga un interés de un 1% anual. Usted sabe también que la tasa de inflación es de un 2% anual. Después de un año, ¿Cuánto sería el valor real del dinero en esta cuenta?',
                'La siguiente frase es verdadera o falsa: «Las acciones son normalmente más riesgosas que los bonos o títulos»',
                'La siguiente frase es verdadera o falsa: «Comprar una acción de una empresa es menos riesgoso que comprar con el mismo dinero varias acciones de distintas empresas»'
                ]
    answers =   [
                '-2',
                '41',
                '114',
                '18',
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
    q1 = models.StringField()
    #q1_cnt_mistakes = models.IntegerField()
    #q1_mistakes = models.StringField()
    q1_time = models.StringField()
    q1_isCorrect = models.StringField()

    q2 = models.StringField()
    #q2_cnt_mistakes = models.IntegerField()
    #q2_mistakes = models.StringField()
    q2_time = models.StringField()
    q2_isCorrect = models.StringField()

    q3 = models.StringField()
    #q3_cnt_mistakes = models.IntegerField()
    #q3_mistakes = models.StringField()
    q3_time = models.StringField()
    q3_isCorrect = models.StringField()

    q4 = models.StringField()
    #q4_cnt_mistakes = models.IntegerField()
    #q4_mistakes = models.StringField()
    q4_time = models.StringField()
    q4_isCorrect = models.StringField()

    q5 = models.StringField()
    #q5_cnt_mistakes = models.IntegerField()
    #q5_mistakes = models.StringField()
    q5_time = models.StringField()
    q5_isCorrect = models.StringField()

    q6 = models.StringField()
    #q6_cnt_mistakes = models.IntegerField()
    #q6_mistakes = models.StringField()
    q6_time = models.StringField()
    q6_isCorrect = models.StringField()

    q7 = models.StringField()
    #q7_cnt_mistakes = models.IntegerField()
    #q7_mistakes = models.StringField()
    q7_time = models.StringField()
    q7_isCorrect = models.StringField()

    q8 = models.StringField()
    #q8_cnt_mistakes = models.IntegerField()
    #q8_mistakes = models.StringField()
    q8_time = models.StringField()
    q8_isCorrect = models.StringField()
    
    cnt_question = models.IntegerField(initial = 1)
