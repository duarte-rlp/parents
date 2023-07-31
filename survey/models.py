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

author = 'Your name here'

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    p_age = models.IntegerField(label="1. Edad")

    p_sex = models.IntegerField(
    choices=[
        [0, 'Hombre'],
        [1, 'Mujer'],
        [2, 'No binario'],
    ], label="2. ¿Con qué género se identifica?")

    p_married = models.IntegerField(
    choices=[
        [1, 'Unión libre'],
        [2, 'Casado (a)'],
        [3, 'Viudo (a)'],
        [4, 'Soltero (a)'],
        [5, 'Divorciado (a)/Separado(a)'],
    ], label="3. Estado civil")
    
    p_family = models.IntegerField(min=0, max=20, label="4. ¿Número de miembros del hogar? (Puede escribir '1' si vive solo)")

    p_children = models.IntegerField(min=0, max=20, label="5. ¿Número de hijos? (Puede escribir '0' si no tiene hijos)")

    p_workers = models.IntegerField(min=0, max=20, label="6. ¿Número de personas que contribuyen a los ingresos del hogar? (Puede escribir '1' si solo una persona trabaja)")
  
    p_educ = models.IntegerField(
    choices=[
        [1,'Ninguno'],
        [2,'Primaria'],
        [3,'Bachillerato'],
        [4,'Técnico o Tecnólogo'],
        [5,'Pregrado'],
        [6,'Posgrado (Especialización, Maestría, Doctorado)']
    ], label="7. ¿Cuál es el nivel educativo más alto que cursó o está cursando?")

    p_job = models.IntegerField(
    choices=[
        [1,'Solo estudio'],
        [2,'Desempleado'],
        [3,'Empleado a jornada completa'],
        [4,'Empleado a tiempo parcial'],
        [5,'Trabajador independiente'],
        [6,'Trabajador no remunerado (por ejemplo: ama de casa, empresa familiar)'],
        [7,'Retirado/pensionado'],
        [8,'Otro'],
        [9,'No sabe']
    ], label="8. ¿Cuál es su situación laboral actual?")

    p_inc = models.IntegerField(
    choices=[
        [1,'Menos de $ 300.000'],
        [2,'Entre $ 300.000 - $ 600.000'],
        [3,'Entre $ 600.000 - $ 900.000'],
        [4,'Entre $ 900.000 - $ 1.200.000'],
        [5,'Entre $ 1.200.000 - $ 1.500.000'],
        [6,'Mayor a $ 1.500.000'],
    ], label="9. ¿Cuál es el rango de su ingreso mensual?")

    p_inc1 = models.CurrencyField(min=c(0), max=c(100000000), label="10. ¿Cuánto es su ingreso mensual?")

    p_ocu = models.IntegerField(
    choices=[
        [1,'Empleado con cargo como director o gerente general'],
        [2,'Empleado de nivel auxiliar o administrativo'],
        [3,'Empleado de nivel directivo'],
        [4,'Empleado de nivel técnico o profesional'],
        [5,'Empleado obrero u operario'],
        [6,'Empresario'],
        [7,'Pequeño empresario'],
        [8,'Profesional independiente'],
        [9,'Trabajador por cuenta propia'],
        [10,'Hogar'],
        [11,'Pensionado'],
        [12,'Desempleado'],
        [13,'Otra actividad u ocupación'],
    ], label="11. ¿Cuál es su ocupación u oficio?")

#    p_risk = models.IntegerField(min=0, max=10, label="9. En una escala del 0 al 10, donde: 0 - significa que no esta dispuesto(a) a tomar riesgos en lo absoluto 10 - significa que esta muy dispuesto(a) a tomar riesgos  Por favor, díga, en general ¿Qué tan dispuesto (a) está o no está usted a tomar riesgos en decisiones financieras?")









