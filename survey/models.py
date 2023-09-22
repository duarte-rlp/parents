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

author = 'hopkeinst'

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

    ## Opciones a las listas de opciones de la encuesta
    gender_list         =   [
                                'Hombre', 
                                'Mujer', 
                                'Otro'
                            ]
    married_list        =   [
                                'Unión libre', 
                                'Casada (o)', 
                                'Viuda (o)', 
                                'Soltera (o)', 
                                'Divorciada (o) / Separada(o)'
                            ]
    education_list      =   [
                                'Ninguno',
                                'Primaria incompleta',
                                'Primaria completa',
                                'Bachillerato incompleto',
                                'Bachillerato completo',
                                'Técnico o Tecnólogo',
                                'Pregrado',
                                'Posgrado (Especialización, Maestría, Doctorado)'
                            ]
    job_list            =   [
                                'Solo estudio',
                                'Desempleado sin buscar trabajo',
                                'Desempleado buscando trabajo',
                                'Empleado a jornada parcial',
                                'Empleado a jornada completa',
                                'Trabajador independiente',
                                'Trabajador no remunerado (por ejemplo: ama de casa, empresa familiar)',
                                'Retirado o pensionado',
                                'Otro / Ninguno'
                            ]
    incomeRange_list    =   [
                                'Menos de $ 300.000',
                                'Entre $ 300.000 - $ 600.000',
                                'Entre $ 600.000 - $ 900.000',
                                'Entre $ 900.000 - $ 1.200.000',
                                'Entre $ 1.200.000 - $ 1.500.000',
                                'Mayor a $ 1.500.000',
                                'Otro / Ninguno'
                            ]
    expenses_list       =   [
                                'Mayores',
                                'Menores',
                                'Iguales'
                            ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q_age           = models.IntegerField()
    q_gender        = models.StringField()
    q_married       = models.StringField()
    q_family        = models.IntegerField()
    q_children      = models.IntegerField()
    q_workers       = models.IntegerField()
    q_educ          = models.StringField()
    q_job           = models.StringField()
    q_income        = models.IntegerField()
    q_incomeRange   = models.StringField()
    q_expenses      = models.StringField()

    
    ########################################################################################################
    #### Risk questions

    p_risk = models.IntegerField(min=0, max=10, label="¿Qué tan dispuesto(a) está o no está usted a tomar riesgos en general? (0 - significa nada dispuesto(a), y 10 - significa muy dispuesto(a))")

    p_risk1 = models.IntegerField(
    choices=[
        [1,'Ningún riesgo'],
        [2,'Pequeño riesgo'],
        [3,'Medio riesgo'],
        [4,'Alto riesgo'],
    ], label="¿Cuándo estás decidiendo sobre tus inversiones que tanto riesgo estás dispuesto a asumir?")

    p_returns = models.IntegerField(min=0, max=10, label="Cuando decide invertir, ¿qué importancia tiene para usted maximizar los retornos? (0 - significa que no es importante, y 10 - significa que es muy importante)")

    p_risk2 = models.IntegerField(min=0, max=10, label="Cuando decide invertir, ¿qué importancia tiene para usted minimizar los riesgos? (0 - significa que no es importante, y 10 - significa que es muy importante)")

    p_loss = models.IntegerField(min=0, max=10, label="Cuando decide invertir, ¿qué importancia tiene para usted minimizar las pérdidas? (0 - significa que no es importante, y 10 - significa que es muy importante)")

    p_insurance = models.IntegerField(
    choices=[
        [1,'Sí'],
        [2,'No'],
        [3,'No lo sé / No me acuerdo'],
    ], label="Durante los últimos 12 meses, usted o algún miembro de su hogar ha contratado o renovado algún seguro de vida, vehículo, terremoto, robo, desempleo u otro seguro, en forma voluntaria?") 

    p_patience = models.IntegerField(min=0, max=10, label="¿Es usted generalmente más paciente o impaciente? (0 - significa muy impaciente, y 10 - significa muy paciente)")

    #### Agriculture and climate

    p_hectareas = models.IntegerField(
    choices=[
        [1,'Ninguna / No trabajo en finca'],
        [2,'Menos de 1 hectárea'],
        [3,'Entre 1 - 3 hectáreas'],
        [4,'Entre 3 - 5 hectáreas'],
        [5,'Entre 5 - 10 hectáreas'],
        [6,'Más que 10 hectáreas'],
        [7,'No lo sé / No me acuerdo'],
    ], label="¿Cuánta superficie dedicada a actividades agricolas o pecuarias manejó el año pasado?")

    p_farminc = models.IntegerField(
    choices=[
        [1,'Cultivos'],
        [2,'Ganado'],
        [3,'No lo sé / No me acerdo'],
        [4,'No trabajo en finca'],
    ], label="¿Cuál es la principal fuente de ingresos de la finca en la que trabaja?")

    p_crops = models.IntegerField(
    choices=[
        [1,'Sólo un cultivo a la vez'],
        [2,'2 cultivos al mismo tiempo'],
        [3,'3 cultivos o más al mismo tiempo'],
        [4,'No cultivo ningún cultivo / No lo sé'],
    ], label="¿Cuando cultiva, cuántos cultivos comerciales diferentes siembra al mismo tiempo?")

    p_crops1 = models.IntegerField(
    choices=[
        [1,'Aguacate'],
        [2,'Arroz'],
        [3,'Banano'],
        [4,'Cacao'],
        [5,'Caña de azúcar'],
        [6, 'Frijol'],
        [7, 'Maíz'],
        [8, 'Pasto'],
        [9, 'Platano'],
        [10, 'Otros'],
        [11, 'No cultivo ningún cultivo / No lo sé'],
    ], label="¿Qué tipo de cultivos siembró el año pasado? (Puede marcar varias opciones)")

    ### insert p_crops2

    p_crops3 = models.IntegerField(
    choices=[
        [1,'Sí, una vez'],
        [2,'Sí, más de una vez'],
        [3,'No, nunca'],
        [4,'No cultivo ningún cultivo / No lo sé'],
    ], label="¿Alguna vez ha experimentado una pérdida de cosechas?")

    p_savings = models.IntegerField(
    choices=[
        [1,'Sí'],
        [2,'No'],
        [3,'No cultivo ningún cultivo / No lo sé'],
    ], label="¿Tiene reservas de dinero o cualquier otra forma de ingreso para protegerse contra pérdidas de cosechas?")

    ### insert p_protection

    p_climate = models.IntegerField(
    choices=[
        [1,'Sí'],
        [2,'No'],
        [3,'No cultivo ningún cultivo / No lo sé'],
    ], label="En su opinión, ¿el cambio climático ya ha afectado la producción agrícola?")

    p_events = models.IntegerField(
    choices=[
        [1,'Incendios forestales'],
        [2,'Inundaciones'],
        [3,'Más lluvia de lo habitual'],
        [4,'Menos lluvia de lo habitual'],
        [5,'Sequías'],
        [6,'Temperaturas más altas de lo habitual'],
        [7,'Temperaturas más bajas de lo habitual'],
        [8,'Terremotos/Temblores'],
        [9,'Otros desastres naturales'],
        [10,'Ningún problema'],
        [11,'No lo sé / No me acuerdo'],
    ], label="Durante los últimos 12 meses, ¿en esta zona o vecindario se presentaron algunos de los siguientes problemas? (Puede marcar varias opciones)")

    p_measures = models.IntegerField(
    choices=[
        [1,'Disponer de los ahorros'],
        [2,'Endeudarse'],
        [3,'Pedir ayuda a un conocido del barrio-vereda'],
        [4,'Pedir ayuda a un familiar'],
        [5,'Vender un activo'],
        [6,'No podria hacer nada y tendría que reducir el consumo'],
    ], label="¿Si estos eventos afectarán negativamente a su hogar, qué medidas tomaría?")





##### Previous questions

    #p_dexpenses = models.IntegerField(
    #choices=[
    #    [1,'Endeudarse'],
    #    [2,'Vender un activo'],
    #    [3,'Disponer de los ahorros'],
    #    [4,'Pedir ayuda a un familiar'],
    #    [5,'Pedir ayuda a un conocido del barrio-vereda'],
    #    [6,'No hubo tales meses'],
    #], label="12. En los meses en que los gastos del hogar han superado los ingresos, ¿qué han hecho para cubrir esta diferencia?")

#    p_risk = models.IntegerField(min=0, max=10, label="9. En una escala del 0 al 10, donde: 0 - significa que no esta dispuesto(a) a tomar riesgos en lo absoluto 10 - significa que esta muy dispuesto(a) a tomar riesgos  Por favor, díga, en general ¿Qué tan dispuesto (a) está o no está usted a tomar riesgos en decisiones financieras?")

#    p_risk = models.IntegerField(
#    choices=[
#        [0,'0 - No estoy dispuesto(a) a tomar riesgos en lo absoluto'],
#        [1,'1'],
#        [2,'2'],
#        [3,'3'],
#        [4,'4'],
#        [5, '5'],
#        [6, '6'],
#        [7, '7'],
#        [8, '8'],
#        [9, '9'],
#        [10, '10 - Muy dispuesto(a) a tomar riesgos'],
#    ], label="¿Qué tan dispuesto(a) está o no está usted a tomar riesgos en general?")

#    p_group = models.IntegerField(
#    choices=[
#        [1,'Cooperativas'],
#        [2,'Gremios'],
#        [3,'Asociación de productores'],
#        [4,'Centros de investigación'],
#        [5,'Organizaciones comunitarias (consejo comunitario, asociación u organización étnica, de mujeres, de ancianos o de jóvenes)'],
#        [6, 'No pertenece a ninguna asociación'],
#        [7, 'No sabe / No responde'],
#    ], label="13. Actualmente el productor pertenece a alguna de las siguientes asociaciones:")

#    p_climate1 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="Nos estamos acercando al límite de la cantidad de personas que la Tierra puede sostener."
#                                       )

#    p_climate2 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="Los seres humanos tienen el derecho de modificar el medio ambiente natural para satisfacer sus necesidades."
#                                       )
#    p_climate3 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="Cuando los seres humanos interfieren con la naturaleza, a menudo producen consecuencias desastrosas."
#                                       )
#    p_climate4 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="El ingenio humano asegurará que no hagamos la Tierra inhabitable."
#                                       )
#    p_climate5 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="Los seres humanos están abusando gravemente de la Tierra."
#                                       )
#    p_climate6 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="La Tierra tiene abundantes recursos naturales si simplemente aprendemos cómo usarlos."
#                                       )
#    p_climate7 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="Las plantas y los animales tienen tanto derecho a existir como los humanos."
#                                       )
#    p_climate8 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="El equilibrio de la naturaleza es lo suficientemente fuerte para hacer frente a los impactos de los países industrializados modernos."
#                                       )
#    p_climate9 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="A pesar de nuestras habilidades especiales, los seres humanos todavía estamos sujetos a las leyes de la naturaleza."
#                                       )
#    p_climate10 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                      widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="La llamada crisis ecológica que enfrenta la humanidad ha sido ampliamente exagerada."
#                                       )
#    p_climate11 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="La Tierra es como una nave espacial con un espacio y recursos muy limitados."
#                                       )
#    p_climate12 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="Los seres humanos estaban destinados a gobernar sobre el resto de la naturaleza."
#                                       )
#    p_climate13 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="El equilibrio de la naturaleza es muy delicado y fácilmente perturbable."
#                                       )
#    p_climate14 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="Los seres humanos eventualmente aprenderán lo suficiente sobre cómo funciona la naturaleza para poder controlarla."
#                                       )
#    p_climate15 = models.PositiveIntegerField(choices=[1,2,3,4,5],
#                                       widget=widgets.RadioSelectHorizontal(),
#                                       verbose_name="Si las cosas siguen su curso actual, pronto experimentaremos una enorme catástrofe ambiental."
#                                       )
#    p_precautions = models.StringField(label="20. ¿Qué medidas preventivas toma para que los cambios de climas no afecten sus ingresos?")
    









