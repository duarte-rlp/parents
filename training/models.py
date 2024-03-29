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

import random


author = '@hopkeinst'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'training'
    players_per_group = None
    num_rounds = 1
    # Datos de inversiones
    inv_labels = [1, 2, 3, 4, 5, 6, 7, 8]
    inv_example = [30, 5, 30, 30, 5, 5, 5, 30] # array exampl for training app
    inv_a = [30, 5, 30, 30, 5, 5, 5, 30]
    inv_b = [0, 0, 25, 0, 25, 25, 0, 25]
    time_steps = 1000 # en milisegundos = 2 segundos
    money_example = 100 # dinero usado para ejemplos
    investment_max = 100 # máxima inversión
    answer_1 = [5, -5] # resultados posibles para la pregunta 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Para almacenar el número ingresado la primera pregunta del training de las gráficas
    test_01_number = models.IntegerField()
    test_01_answer = models.StringField() # 
    test_01_time = models.StringField() # tiempo que demora en presionar continuar

    # Con dos series de datos al tiempo
    test_02_number = models.IntegerField()
    test_02_answer = models.StringField() # 
    test_02_time = models.StringField() # tiempo que demora en presionar continuar

    test_03_number = models.IntegerField()
    test_03_answer = models.StringField() # 
    test_03_time = models.StringField() # tiempo que demora en presionar continuar

    test_04_number = models.IntegerField()
    test_04_answer = models.StringField() # 
    test_04_time = models.StringField() # tiempo que demora en presionar continuar

    test_05_number_a = models.IntegerField()
    test_05_answer_a = models.StringField()
    test_05_number_b = models.IntegerField()
    test_05_answer_b = models.StringField()
    test_05_time = models.StringField() # tiempo que demora en presionar continuar

    test_06_number_a = models.IntegerField()
    test_06_answer_a = models.StringField()
    test_06_number_b = models.IntegerField()
    test_06_answer_b = models.StringField()
    test_06_time = models.StringField() # tiempo que demora en presionar continuar

# Las del ejemplo
    test_07_number_a = models.IntegerField()
    test_07_number_b = models.IntegerField()
    test_07_mistakes = models.StringField()
    test_07_time = models.StringField() # tiempo que demora en presionar continuar



