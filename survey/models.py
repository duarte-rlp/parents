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
        [2,'Primaria incompleta'],
        [3,'Primaria completa'],
        [4,'Bachillerato incompleto'],
        [5,'Bachillerato completo'],
        [6,'Técnico o Tecnólogo'],
        [7,'Pregrado'],
        [8,'Posgrado (Especialización, Maestría, Doctorado)']
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
    ], label="9. ¿En qué rango se encuentra su ingreso mensual?")

    p_inc1 = models.CurrencyField(min=c(0), max=c(100000000), label="10. ¿Cuánto es su ingreso mensual?")

    p_debt = models.IntegerField(
    choices=[
        [1,'Mayores'],
        [2,'Menores'],
        [3,'Iguales'],
    ], label="11. En el último mes los gastos del hogar frente a sus ingresos han sido:")

    p_debt1 = models.IntegerField(
    choices=[
        [1,'Endeudarse'],
        [2,'Vender un activo'],
        [3,'Disponer de los ahorros'],
        [4,'Pedir ayuda a un familiar'],
        [5,'Pedir ayuda a un conocido del barrio-vereda'],
        [6, 'No hubo tales meses'],
    ], label="12. En los meses en que los gastos del hogar han superado los ingresos, ¿qué han hecho para cubrir esta diferencia? (Puede marcar varias opciones)")

    p_prod = models.IntegerField(
    choices=[
        [1,'Cooperativas'],
        [2,'Gremios'],
        [3,'Asociación de productores'],
        [4,'Centros de investigación'],
        [5,'Organizaciones comunitarias (consejo comunitario, asociación u organización étnica, de mujeres, de ancianos o de jóvenes)'],
        [6, 'No pertenece a ninguna asociación'],
        [7, 'No sabe / No responde'],
    ], label="13. Actualmente el productor pertenece a alguna de las siguientes asociaciones: (Puede marcar varias opciones)")

    p_insurance = models.IntegerField(
    choices=[
        [1,'Sí'],
        [2,'No'],
        [3,'No sabe / No responde'],
    ], label="14. Durante los últimos 12 meses, usted o algún miembro de su hogar ha contratado o renovado algún seguro de vida, vehículo, terremoto, robo, desempleo u otro seguro, en forma voluntaria?")

    p_insurance1 = models.IntegerField(
    choices=[
        [1,'Sí'],
        [2,'No'],
        [3,'No sabe / No responde'],
    ], label="15. ¿Considera que cuando deje de trabajar podrá solventar los gastos de su hogar con sus ahorros para la vejez?")

    p_insurance2 = models.IntegerField(
    choices=[
        [1,'Aportando en un fondo de pensiones obligatorias'],
        [2,'Aportando en un fondo de pensiones voluntarias (por ejemplo, BEPS)'],
        [3,'Ahorrando'],
        [4,'Haciendo inversiones'],
        [5,'Pagando un seguro por su cuenta'],
        [6, 'Preparando a sus hijos para que puedan ayudarlo en su vejez'],
        [7, 'Nada'],
        [8, 'No sabe / No responde'],
    ], label="16. ¿Qué está haciendo USTED para mantenerse económicamente en la vejez? (Puede marcar varias opciones)")

    p_events = models.IntegerField(
    choices=[
        [1,'Enfrentamientos entre grupos armados'],
        [2,'Atentados terroristas'],
        [3,'Inundaciones'],
        [4,'Terremotos/Temblores'],
        [5,'Más lluvia de lo habitual'],
        [6, 'Sequías'],
        [7, 'Otros desastres naturales'],
        [8, 'Ningún problema'],
        [9, 'No sabe / No responde'],
    ], label="17. Durante los últimos 12 meses, ¿en esta zona o vecindario se presentaron algunos de los siguientes problemas? (Puede marcar varias opciones)")

    p_clima = models.IntegerField(
    choices=[
        [1,'Ahorro'],
        [2,'Endeudamiento'],
        [3,'Inversión'],
        [4,'No tiene en cuenta los cambios de clima'],
    ], label="18. ¿Para cuál de las siguientes decisiones tiene en cuenta el cambio del clima? (Puede marcar varias opciones)")

    p_clima1 = models.IntegerField(
    choices=[
        [1,'Invierno'],
        [2,'Verano'],
    ], label="19. ¿Qué estación del año prefiere? (Puede marcar varias opciones)")

    p_clima2 = models.StringField(label="20. ¿Qué medidas preventivas toma para que los cambios de climas no afecten sus ingresos?")

#    p_risk = models.IntegerField(min=0, max=10, label="9. En una escala del 0 al 10, donde: 0 - significa que no esta dispuesto(a) a tomar riesgos en lo absoluto 10 - significa que esta muy dispuesto(a) a tomar riesgos  Por favor, díga, en general ¿Qué tan dispuesto (a) está o no está usted a tomar riesgos en decisiones financieras?")









