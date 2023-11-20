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
    risk_list           =   [
                                'Ningún riesgo',
                                'Pequeño riesgo',
                                'Medio riesgo',
                                'Alto riesgo'
                            ]
    insurance_list      =   [
                                'Si',
                                'No',
                                'No lo sé / No me acuerdo'
                            ]
    hectares_list       =   [
                                'Ninguna / No trabajo en finca',
                                'Menos de 1 hectárea',
                                'Entre 1 - 3 hectáreas',
                                'Entre 3 - 5 hectáreas',
                                'Entre 5 - 10 hectáreas',
                                'Más que 10 hectáreas',
                                'No lo sé / No me acuerdo'
                            ]
    farminc_list        =   [
                                'Cultivos',
                                'Ganado',
                                'Pescado',
                                'No lo sé / No me acuerdo',
                                'No trabajo en finca'
                            ]
    crops_list          =   [
                                'Sólo un cultivo a la vez',
                                '2 cultivos al mismo tiempo',
                                '3 o más cultivos al mismo tiempo',
                                'No trabajo en finca / No lo sé'
                            ]
    cropTypes_list      =   [
                                'Aguacate',
                                'Arroz',
                                'Banano',
                                'Cacao',
                                'Caña de azúcar',
                                'Frijol',
                                'Maíz',
                                'Pasto',
                                'Platano',
                                'Otros',
                                'No trabajo en finca / No lo sé'
                            ]
    cropImportance_list =   [
                                'Rendimientos en años anteriores',
                                'Rendimientos esperados el próximo año',
                                'Clima en los años anteriores',
                                'Clima esperado para el próximo año',
                                'Conocimiento sobre cómo realizar los cultivos',
                                'Los cultivos que se están realizando en otras fincas de la región'
                            ]
    cropsLoss_list      =   [
                                'Sí, una vez',
                                'Sí, más de una vez',
                                'No, nunca',
                                'No trabajo en finca / No lo sé'
                            ]
    savings_list        =   [
                                'Si',
                                'No',
                                'No trabajo en finca / No lo sé'
                            ]
    protection_list     =   [
                                'Tener ahorros para poder usar en caso de pérdida de ingresos',
                                'Tener diferentes tipos de cultivos para evitar pérdidas',
                                'Tener ganado para compensar pérdidas en cultivos',
                                'Tener otras fuentes de ingresos además de la granja (por ejemplo: otro trabajo u ocupación)',
                                'Tener un seguro contra pérdidas de cosechas (por ejemplo: seguro contra el mal clima)',
                                'Pedir ayuda de familiares o amigos en tales casos'
                                'No trabajo en finca / No lo sé'
                            ]
    climate_list        =   [
                                'Si',
                                'No',
                                'No trabajo en finca / No lo sé'
                            ]
    events_list         =   [
                                'Incendios forestales',
                                'Inundaciones',
                                'Más lluvia de lo habitual',
                                'Menos lluvia de lo habitual',
                                'Sequías',
                                'Temperaturas más altas de lo habitual',
                                'Temperaturas más bajas de lo habitual',
                                'Terremotos/Temblores',
                                'Otros desastres naturales',
                                'Ningún problema',
                                'No lo sé / No me acuerdo'
                            ]
    measures_list       =   [
                                'Disponer de los ahorros',
                                'Endeudarse',
                                'Pedir ayuda a un conocido del barrio-vereda',
                                'Pedir ayuda a un familiar',
                                'Vender un activo',
                                'No podria hacer nada y tendría que reducir el consumo'
                            ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

# Initial Questions
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

# Risk Questions
    q_risk          = models.IntegerField()
    q_riskList      = models.StringField()
    q_returns       = models.IntegerField()
    q_riskImportant = models.IntegerField()
    q_loss          = models.IntegerField()
    q_insurance     = models.StringField()
    q_patience      = models.IntegerField()

# Agriculture & Climate Questions
    q_hectares      = models.StringField()
    q_farminc       = models.StringField()
    q_crops         = models.StringField()
    q_cropTypes     = models.StringField()
    q_cropsImp_1    = models.IntegerField()
    q_cropsImp_2    = models.IntegerField()
    q_cropsImp_3    = models.IntegerField()
    q_cropsImp_4    = models.IntegerField()
    q_cropsImp_5    = models.IntegerField()
    q_cropsImp_6    = models.IntegerField()
    q_cropsLoss     = models.StringField()
    q_savings       = models.StringField()
    q_protection_1  = models.IntegerField()
    q_protection_2  = models.IntegerField()
    q_protection_3  = models.IntegerField()
    q_protection_4  = models.IntegerField()
    q_protection_5  = models.IntegerField()
    q_protection_6  = models.IntegerField()
    q_climate       = models.StringField()
    q_events        = models.StringField()
    q_measures      = models.StringField()





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
    









