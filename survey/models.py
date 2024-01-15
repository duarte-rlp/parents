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
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

    ## Opciones a las listas de opciones de la encuesta
    gender_list         =   [
                                'Homem', 
                                'Mulher', 
                                'Outro'
                            ]
    married_list        =   [
                                'Solteiro(a)',
                                'União estável', 
                                'Casado(a)', 
                                'Viúvo(a)',  
                                'Divorciado(a) / Separado(a)'
                            ]
    education_list      =   [
                                'Nenhum',
                                'Primário incompleto',
                                'Primário completo',
                                'Ensino médio incompleto',
                                'Ensino médio completo',
                                'Ensino técnico incompleto',
                                'Ensino técnico completo',
                                'Bacharelado incompleto',
                                'Bacharelado completo',
                                'Pós-Graduação (especialização, mestrado, doutorado)'
                            ]
    job_list            =   [
                                'Estudante',
                                'Desempregado(a) sem procurar trabalho',
                                'Desempregado(a) à procura de trabalho',
                                'Empregado(a) em meio período',
                                'Empregado(a) em período integral',
                                'Autônomo(a)',
                                'Trabalhador(a) não remunerado (por exemplo: dono(a) de casa, em empresa familiar)',
                                'Aposentado(a) ou pensionista',
                                'Outro / Nenhum'
                            ]
    incomeRange_list    =   [
                                'Menos de R$ 1.500',
                                'Entre R$ 1.500 e R$ 3.200',
                                'Entre R$ 3.200 e R$ 7.600',
                                'Entre R$ 7.600 e R$ 23.800',
                                'Acima de R$ 23.800',
                                'Outro / Nenhum'
                            ]
    expenses_list       =   [
                                'Maiores',
                                'Menores',
                                'Iguais'
                            ]
    devices_list        =   [
                                'Computador',
                                'Tablet',
                                'Celular'
                            ]
    risk_list           =   [
                                'Nenhum risco',
                                'Pequeno risco',
                                'Médio risco',
                                'Alto risco'
                            ]
    insurance_list      =   [
                                'Sim',
                                'Não',
                                'Não sei / Não me lembro'
                            ]
    hectares_list       =   [
                                'Não trabalho com agro / Nenhum',
                                'Menos de 1 hectare',
                                'Entre 1 e 3 hectares',
                                'Entre 3 e 5 hectares',
                                'Entre 5 e 10 hectares',
                                'Mais que 10 hectares',
                                'Não sei / Não me lembro'
                            ]
    farminc_list        =   [
                                'Não trabalho com agro',
                                'Cultivos',
                                'Gado',
                                'Pesca',
                                'Não sei/Não me lembro'
                            ]
    crops_list          =   [
                                'Não trabalho com agro / Não sei',
                                'Apenas um cultivo de cada vez',
                                '2 cultivos ao mesmo tempo',
                                '3 ou mais cultivos ao mesmo tempo'
                            ]
    cropTypes_list      =   [
                                'Não trabalho com agro / Não sei',
                                'Hortaliças (por exemplo: alface, rúcula, agrião)',
                                'Frutas (por exemplo: laranja, banana)',
                                'Vegetais (por exemplo: abobrinha, chuchu, etc.)',
                                'Grãos (por exemplo: arroz, feijão, etc.)',
                                'Tubérculos (por exemplo: batata, mandioca, etc.)',
                                'Cana de açúcar',
                                'Soja',
                                'Milho',
                                'Pasto',
                                'Outros'
                            ]
    cropImportance_list =   [
                                'Não trabalho com agro',
                                'Desempenhos em anos anteriores',
                                'Retornos esperados para o próximo ano',
                                'Clima em anos anteriores',
                                'Clima esperado para o próximo ano',
                                'Meu conhecimento sobre como cultivar',
                                'Os cultivos que outros agricultores da região estão cultivando'
                            ]
    cropsLoss_list      =   [
                                'Não trabalho com agro / Não sei',
                                'Sim uma vez',
                                'Sim, mais de uma vez',
                                'Não, nunca'
                            ]
    savings_list        =   [
                                'Não trabalho com agro / Não sei',
                                'Sim',
                                'Não'
                            ]
    protection_list     =   [
                                'Não trabalho com agro / Não sei',
                                'Ter poupança para poder utilizar em caso de quebra de safra',
                                'Ter diferentes tipos de cultivos para evitar perdas',
                                'Ter gado para compensar as perdas nas colheitas',
                                'Ter outras fontes de renda além do agro (por exemplo: outro emprego ou ocupação)',
                                'Ter seguro contra quebras de safra (por exemplo: seguro contra intempéries)',
                                'Pedir ajuda de familiares ou amigos nesses casos'
                            ]
    climate_list        =   [
                                'Não trabalho com agro / Não sei',
                                'Sim',
                                'Não'
                            ]
    events_list         =   [
                                'Incêndios florestais',
                                'Inundações',
                                'Mais chuva que o normal',
                                'Menos chuva que o normal',
                                'Secas',
                                'Temperaturas mais altas que o normal',
                                'Temperaturas mais baixas que o normal',
                                'Terremotos / Tremores',
                                'Outros desastres naturais',
                                'Nenhum problema',
                                'Não sei / não me lembro'
                            ]
    measures_list       =   [
                                'Usar as economias próprias',
                                'Fazer uma dívida',
                                'Pedir ajuda a alguém conhecido',
                                'Pedir ajuda a um membro da família',
                                'Vender algo de valor',
                                'Reduzir as compras'
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
    q_device        = models.StringField()

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
    









