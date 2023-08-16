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


author = 'Ferley, Jorge'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'training'
    players_per_group = None
    num_rounds = 1
    # Datos de inversiones
    inv_labels = [1, 2, 3, 4, 5, 6, 7, 8]
    inv_example = [15, -8, 15, 15, -8, -8, -8, 15] # array exampl for training app
    inv_a = [15, -8, 15, 15, -8, -8, -8, 15]
    inv_b = [-9, -9, 14, -9, 14, 14, -9, 14]
    time_steps = 200 # en milisegundos = 2 segundos
    money_example = 100 # dinero usado para ejemplos


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



    # Almacenar lo relacionado a la posición de la carta
    test_06_cardIndex = models.IntegerField()

    # Almacenar el ejemplo del slider
    slider_example = models.IntegerField()
    # Almacenar el random del ejemplo
    test_07_cardIndex = models.IntegerField()
    test_07_payment = models.IntegerField()
    test_07_answer = models.IntegerField()

