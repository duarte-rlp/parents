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
    name_in_url = 'allocations'
    players_per_group = None
    num_rounds = 1
    # Datos de inversiones
    inv_labels = [1, 2, 3, 4, 5, 6, 7, 8]
    inv_example = [10, 10, 10, 10, -5, -5, -5, -5]
    inv_a = [15, 15, 15, 15, -8, -8, -8, -8]
    #random.shuffle(inv_a) # si se desea que el orden sea aleatorio
    inv_b = [-9, -9, -9, -9, 14, 14, 14, 14]
    #random.shuffle(inv_b) # si se desea que el orden sea aleatorio


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Para almacenar el número ingresado la primera pregunta del retorno de la primera carta, así como si fue correcto o no
    test_01_number = models.IntegerField()
    test_01_answer = models.IntegerField() # 0 -> respuesta incorrecta | 1 -> respuesta correcta

    # Para almacenar el número ingresado la segunda pregunta del retorno de la última carta, así como si fue correcto o no
    test_02_number = models.IntegerField()
    test_02_answer = models.IntegerField() # 0 -> respuesta incorrecta | 1 -> respuesta correcta

    # Para almacenar las respuestas de la cantidad de cartas positivas
    test_03_A_number = models.IntegerField()
    test_03_A_answer = models.IntegerField() # 0 -> respuesta incorrecta | 1 -> respuesta correcta
    test_03_B_number = models.IntegerField()
    test_03_B_answer = models.IntegerField() # 0 -> respuesta incorrecta | 1 -> respuesta correcta

    # Para almacenar las respuestas de la cantidad de cartas negativas
    test_04_A_number = models.IntegerField()
    test_04_A_answer = models.IntegerField() # 0 -> respuesta incorrecta | 1 -> respuesta correcta
    test_04_B_number = models.IntegerField()
    test_04_B_answer = models.IntegerField() # 0 -> respuesta incorrecta | 1 -> respuesta correcta

    # Almacenar lo relacionado a la posición de la carta
    test_05_cardIndex = models.IntegerField()
    # Y los valores que se consultan después relacionado a estos
    test_05_A_number = models.IntegerField()
    test_05_A_answer = models.IntegerField()
    test_05_B_number = models.IntegerField()
    test_05_B_answer = models.IntegerField()

    # Almacenar lo relacionado a la posición de la carta
    test_06_cardIndex = models.IntegerField()

    # Almacenar el ejemplo del slider
    slider_example = models.IntegerField()
    # Almacenar el random del ejemplo
    test_07_cardIndex = models.IntegerField()
    test_07_payment = models.IntegerField()
    test_07_answer = models.IntegerField()

