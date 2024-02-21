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
                'Quanto é 18 - 20?',
                'Quanto é 60 - 19?',
                'Quanto é 6 x 20?',
                'Quanto é 10% de 200?',
                'Suponha que você tem R$ 100 em um investimento que paga juros anuais de 2%. Se o investimento for guardado por 5 anos, sem efetuar nenhum outro pagamento ou sacar o dinheiro, quanto você terá ao final desses 5 anos?',
                'Suponha que sua conta poupança pague juros de 1% ao ano. Você também sabe que a taxa de inflação é de 2% ao ano. Após um ano, quanto seria o valor real do dinheiro nesta conta poupança?',
                'Verdadeiro ou falso: "As ações são geralmente mais arriscadas do que títulos de tesouro direto ou renda fixa"',
                'Verdadeiro ou falso: "Comprar uma ação de uma empresa é menos arriscado do que comprar várias ações de empresas diferentes com o mesmo dinheiro."'
                ]
    answers =   [
                '-2',
                '41',
                '120',
                '20',
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
