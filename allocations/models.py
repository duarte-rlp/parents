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

import pandas as pd
import random

author = '@hopkeinst'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'allocations'
    players_per_group = None
    num_rounds = 1
    inv_labels = [1, 2, 3, 4, 5, 6, 7, 8]
    max_inv = 100

    # Problema de -50%
    problem_01 = pd.DataFrame({
        'Col_A': [
            60,
            60,
            60,
            60,
            10,
            10,
            10,
            10
            ],
        'Col_B': [
            0,
            0,
            0,
            50,
            50,
            50,
            50,
            0
            ]
        }, index = [1, 2, 3, 4, 5, 6, 7, 8])

    # Problema de 0%
    problem_02 = pd.DataFrame({
        'Col_A': [
            60,
            60,
            60,
            60,
            10,
            10,
            10,
            10
            ],
        'Col_B': [
            0,
            0,
            50,
            50,
            50,
            50,
            0,
            0
            ]
        }, index = [1, 2, 3, 4, 5, 6, 7, 8])

    # Problema de 50%
    problem_03 = pd.DataFrame({
        'Col_A': [
            60,
            60,
            60,
            60,
            10,
            10,
            10,
            10
            ],
        'Col_B': [
            0,
            50,
            50,
            50,
            50,
            0,
            0,
            0
            ]
        }, index = [1, 2, 3, 4, 5, 6, 7, 8])

    # Problema de 100%
    problem_04 = pd.DataFrame({
        'Col_A': [
            60,
            60,
            60,
            60,
            10,
            10,
            10,
            10
            ],
        'Col_B': [
            50,
            50,
            50,
            50,
            0,
            0,
            0,
            0
            ]
        }, index = [1, 2, 3, 4, 5, 6, 7, 8])

    # List of the problems
    problems = [problem_01, problem_02, problem_03, problem_04]
    # Numbers of problems 0 -> n
    n_problems = list(range(len(problems)))
    name_problems = ['-50%', '0%', '+50%', '+100%']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # El orden de los problemas
    name_order_problems = models.StringField()
    n_order_problems = models.StringField()
    # El orden de la column 0 -> decreciente | 1 -> ascendente
    order_problem_01_a = models.IntegerField()
    order_problem_01_b = models.IntegerField()
    order_problem_02_a = models.IntegerField()
    order_problem_02_b = models.IntegerField()
    order_problem_03_a = models.IntegerField()
    order_problem_03_b = models.IntegerField()
    order_problem_04_a = models.IntegerField()
    order_problem_04_b = models.IntegerField()
    # Saber cual es la primera columna, la inversión A
    assetA_problem_01 = models.IntegerField()
    assetA_problem_02 = models.IntegerField()
    assetA_problem_03 = models.IntegerField()
    assetA_problem_04 = models.IntegerField()

    # Datos sobre problemas ya reorganizados
    problem_01_type = models.StringField()
    problem_01_inv_a = models.StringField()
    problem_01_order_a = models.StringField()
    problem_01_order_b = models.StringField()
    problem_01_btnSelected = models.StringField()
    problem_01_btnTime = models.StringField()
    problem_01_sliderSelected = models.StringField()
    problem_01_sliderTime = models.StringField()
    problem_01_sliderInv_a = models.IntegerField()
    problem_01_invCntMistakers = models.StringField()
    problem_01_invMistakes = models.StringField()
    problem_01_invTime = models.StringField()
    problem_01_invVal_a = models.IntegerField()
    problem_01_invVal_b = models.IntegerField()
    '''
    problem_01_return_b = models.IntegerField()
    problem_01_expect_return_b = models.IntegerField()
    problem_01_probability_b = models.IntegerField()
    problem_01_risk = models.IntegerField()
    problem_01_insurance = models.IntegerField()
    '''

    problem_02_type = models.StringField()
    problem_02_inv_a = models.StringField()
    problem_02_order_a = models.StringField()
    problem_02_order_b = models.StringField()
    problem_02_btnSelected = models.StringField()
    problem_02_btnTime = models.StringField()
    problem_02_sliderSelected = models.StringField()
    problem_02_sliderTime = models.StringField()
    problem_02_sliderInv_a = models.IntegerField()
    problem_02_invCntMistakers = models.StringField()
    problem_02_invMistakes = models.StringField()
    problem_02_invTime = models.StringField()
    problem_02_invVal_a = models.IntegerField()
    problem_02_invVal_b = models.IntegerField()
    '''
    problem_02_return_b = models.IntegerField()
    problem_02_expect_return_b = models.IntegerField()
    problem_02_probability_b = models.IntegerField()
    problem_02_risk = models.IntegerField()
    problem_02_insurance = models.IntegerField()
    '''

    problem_03_type = models.StringField()
    problem_03_inv_a = models.StringField()
    problem_03_order_a = models.StringField()
    problem_03_order_b = models.StringField()
    problem_03_btnSelected = models.StringField()
    problem_03_btnTime = models.StringField()
    problem_03_sliderSelected = models.StringField()
    problem_03_sliderTime = models.StringField()
    problem_03_sliderInv_a = models.IntegerField()
    problem_03_invCntMistakers = models.StringField()
    problem_03_invMistakes = models.StringField()
    problem_03_invTime = models.StringField()
    problem_03_invVal_a = models.IntegerField()
    problem_03_invVal_b = models.IntegerField()
    '''
    problem_03_return_b = models.IntegerField()
    problem_03_expect_return_b = models.IntegerField()
    problem_03_probability_b = models.IntegerField()
    problem_03_risk = models.IntegerField()
    problem_03_insurance = models.IntegerField()
    '''

    problem_04_type = models.StringField()
    problem_04_inv_a = models.StringField()
    problem_04_order_a = models.StringField()
    problem_04_order_b = models.StringField()
    problem_04_btnSelected = models.StringField()
    problem_04_btnTime = models.StringField()
    problem_04_sliderSelected = models.StringField()
    problem_04_sliderTime = models.StringField()
    problem_04_sliderInv_a = models.IntegerField()
    problem_04_invCntMistakers  = models.StringField()
    problem_04_invMistakes = models.StringField()
    problem_04_invTime = models.StringField()
    problem_04_invVal_a = models.IntegerField()
    problem_04_invVal_b = models.IntegerField()
    '''
    problem_04_return_b = models.IntegerField()
    problem_04_expect_return_b = models.IntegerField()
    problem_04_probability_b = models.IntegerField()
    problem_04_risk = models.IntegerField()
    problem_04_insurance = models.IntegerField()
    '''

    # Variables para el caso de -50%
    problem_minus50perc_return_b = models.IntegerField()
    problem_minus50perc_expect_return_b = models.IntegerField()
    problem_minus50perc_probability_b = models.IntegerField()
    problem_minus50perc_risk = models.IntegerField()
    problem_minus50perc_insurance = models.IntegerField()

    # Variables para los pagos
    n_problem = models.IntegerField() # El problema escogido, de los 4
    n_scene = models.IntegerField() # El escenario escogido de los 8, del problema escogido
    per_investment_1 = models.IntegerField() # El porcentaje de la inversión A del escenario y problema escogido
    per_investment_2 = models.IntegerField() # El porcentaje de la inversión B del escenario y problema escogido
    val_invesment_1 = models.IntegerField() # El dinero que se da la inversión A en el problema escogido
    val_invesment_2 = models.IntegerField() # El dinero que se da la inversión B en el problema escogido
    amount_invesment_1 = models.IntegerField() # El total calculado para la inversión A del escenario y problema escogido
    amount_invesment_2 = models.IntegerField() # El total calculado para la inversión B del escenario y problema escogido
    payoff_amount_app = models.IntegerField() # Total que se paga por esta app

    name_app_n = models.IntegerField(default = 2)
    name_app = models.StringField(default = 'allocations')
    name_app_2_user = models.StringField(default = 'Decisiones de inversión')


