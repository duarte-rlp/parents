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
    table_options = {
        0: {'label': 'Estudiando', 'name': '_study'},
        1: {'label': 'Prestando servicio militar', 'name': '_militar'},
        2: {'label': 'Trabajando por un salario para un empleador', 'name': '_worker'},
        3: {'label': 'Trabajando por cuenta propia', 'name': '_selfemployed'},
        4: {'label': 'Trabajando con familiares sin remuneración', 'name': '_nonwage'},
        5: {'label': 'No este trabajando, ni estudiando', 'name': '_nini'}
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prueba_20000 = models.StringField();
    prueba_15000 = models.StringField();
    prueba_10000 = models.StringField();
    prueba_5000 = models.StringField();

    puntaje_20000 = models.IntegerField();
    puntaje_15000 = models.IntegerField();
    puntaje_10000 = models.IntegerField();
    puntaje_5000 = models.IntegerField();

    prefer_20000 = models.IntegerField();
    prefer_15000 = models.IntegerField();
    prefer_10000 = models.IntegerField();
    prefer_5000 = models.IntegerField();

    grupo_puntaje_global = models.IntegerField();

    # Variables para tablas de 'de la escuela al trabajo'
    l_study         = models.IntegerField();
    l_militar       = models.IntegerField();
    l_worker        = models.IntegerField();
    l_selfemployed  = models.IntegerField();
    l_nonwage       = models.IntegerField();
    l_nini          = models.IntegerField();
    m_study         = models.IntegerField();
    m_militar       = models.IntegerField();
    m_worker        = models.IntegerField();
    m_selfemployed  = models.IntegerField();
    m_nonwage       = models.IntegerField();
    m_nini          = models.IntegerField();
    h_study         = models.IntegerField();
    h_militar       = models.IntegerField();
    h_worker        = models.IntegerField();
    h_selfemployed  = models.IntegerField();
    h_nonwage       = models.IntegerField();
    h_nini          = models.IntegerField();

    educ_type = models.IntegerField(
    choices=[
        [1,'Técnica'],
        [2,'Tecnológica'],
        [3,'Profesional'],
        [4,'Ninguna']
    ], label="¿Para hacer lo que más le gusta es necesaria una carrera?")

    educ_university = models.StringField(label="Escriba el nombre de la institución educativa en la que desea estudiar. También puede escribir NO SÉ")
    educ_university2 = models.StringField(label="¿Tiene una segunda opción? En caso de que sí, escriba el nombre de la institución educativa donde también le gustaría estudiar. También puede escribir NO SÉ o NO TENGO SEGUNDA OPCIÓN:")

    efficacy =  models.IntegerField()  #Pruebas
    check_slider_efficacy =  models.IntegerField()

    efficacy1 =  models.IntegerField() #Técnico
    check_slider_efficacy1 =  models.IntegerField()

    efficacy2 =  models.IntegerField() #Militar
    check_slider_efficacy2 =  models.IntegerField()

    efficacy3 =  models.IntegerField() #Emprendedor
    check_slider_efficacy3 =  models.IntegerField()

    efficacy4 =  models.IntegerField() #Título profesional
    check_slider_efficacy4 =  models.IntegerField()


    educ_inc1 =  models.IntegerField() 
    check_slider_educ_inc1 =  models.IntegerField()

    educ_inc2 =  models.IntegerField() 
    check_slider_educ_inc2 =  models.IntegerField()

    educ_inc3 =  models.IntegerField() 
    check_slider_educ_inc3 =  models.IntegerField()

    educ_inc4 =  models.IntegerField() 
    check_slider_educ_inc4 =  models.IntegerField()

    educ_inc5 =  models.IntegerField() 
    check_slider_educ_inc5 =  models.IntegerField()



    educsup =  models.IntegerField()
    check_slider_educsup=  models.IntegerField()

    educ_barrier1 =  models.IntegerField()
    check_slider_educ_barrier1=  models.IntegerField()

    educ_barrier2 =  models.IntegerField()
    check_slider_educ_barrier2=  models.IntegerField()

    educ_barrier3 =  models.IntegerField()
    check_slider_educ_barrier3=  models.IntegerField()

    educ_barrier4 =  models.IntegerField()
    check_slider_educ_barrier4=  models.IntegerField()

    educ_barrier5 =  models.IntegerField()
    check_slider_educ_barrier5=  models.IntegerField()

    educ_barrier6 =  models.IntegerField()
    check_slider_educ_barrier6=  models.IntegerField()

    educ_barrier7 =  models.IntegerField()
    check_slider_educ_barrier7=  models.IntegerField()


    p_vocational = models.IntegerField(
    choices=[
        [1, 'Sí'],
        [2, 'No'],
    ], label="1. ¿Ha participado antes en alguna actividad de orientación vocacional/profesional?")

    p_preicfes = models.IntegerField(
    choices=[
        [1, 'Sí'],
        [2, 'Sí, en el colegio y NO tuve que pagar'],
        [3, 'Sí, en el colegio y tuve que pagar'],
        [4, 'Sí, fuera del colegio y NO tuve que pagar'],
        [5, 'Sí, fuera del colegio y tuve que pagar'],

    ], label="2. ¿Ha participado antes en alguna actividad de preparación para el Saber 11 (pre-icfes)?")

    p_sex = models.IntegerField(
    choices=[
        [1, 'Hombre'],
        [2, 'Mujer'],
        [3, 'Otro'],
    ], label="3. ¿Cuál es su sexo?")

    p_age = models.IntegerField(label="4. Edad")

    p_work = models.IntegerField(
    choices=[
        [1, 'No, solo estudio.'],
        [2, 'Sí, para ganar dinero para mis gastos.'],
        [3, 'Sí, para ayudar con los gastos familiares.'],
        [4, 'Sí, para obtener experiencia laboral.'],
        [5, 'Sí, para ganar dinero para mis gastos'],
        [6, 'Sí, para hacer contactos que podrían llevarle a encontrar un trabajo. '],
        [7, 'Sí, por otra razón '],
    ], label="5. ¿Ha trabajado y estudiado al mismo tiempo? ¿Cuál fue su motivo principal para trabajar mientras estudiaba?")

    p_hwork = models.IntegerField(min=0, max=48, label="6. ¿Cuántas horas trabajó usted durante la semana pasada? (puede escribir 0)")

    p_wage = models.IntegerField(
    choices=[
        [1, 'No.'],
        [2, 'Si, en efectivo.'],
        [3, 'Si, en especie.'],
        [4, 'Si, en efectivo y especie.'],
    ], label="7. ¿Usted recibe algún tipo de remuneración por trabajar?")

    p_desertion = models.IntegerField(
    choices=[
        [1, 'No.'],
        [2, 'Sí, por dificultades académicas.'],
        [3, 'Sí, por dificultades en el colegio con compañeros, docentes o directivos.'],
        [4, 'Sí, por enfermedad.'],
        [5, 'Sí, por falta de interés en estudiar.'],
        [6, 'Sí, por razones económicas.'],
        [7, 'Sí, por razones de seguridad (nivel de violencia en la zona).'],
    ], label="8. ¿Alguna vez tuvo que suspender sus estudios?")

    p_years = models.IntegerField(
    choices=[
        [1, 'No, no he perdido ningún año.'],
        [2, 'Sí, estudié y no aprobé los exámenes.'],
        [3, 'Sí, por dificultades en el colegio con compañeros, docentes o directivos.'],
        [4, 'Sí, por enfermedad.'],
        [5, 'Sí, no me interesaban los temas.'],
        [6, 'Sí, por razones económicas.'],
        [7, 'Sí, tenía poco tiempo después del colegio para estudiar.'],
        [8, 'Sí, por razones de seguridad (nivel de violencia en la zona).']
    ], label="9. ¿Ha reprobado algún año?")

    p_internet = models.IntegerField(
    choices=[
        [1, 'No.'],
        [2, 'Sí, al menos un teléfono móvil con datos.'],
        [3, 'Sí, un computador portátil con conexión a internet.'],
        [4, 'Sí, un computador de escritorio con conexión a internet.'],
    ], label="10. ¿En su hogar cuenta con acceso o conexión a internet?")

    p_tinternet = models.IntegerField(
    choices=[
        [1, 'No Navega en Internet'],
        [2, '30 minutos o menos'],
        [3, 'Entre 30 y 60 minutos'],
        [4, 'Entre 1 y 3 horas'],
        [5, 'Más de 3 horas'],
    ], label="11. Usualmente, ¿cuánto tiempo al DÍA dedica a navegar en internet?")

    p_care = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    widget=widgets.RadioSelectHorizontal,
    label="12. De 1 (nada) a 5 (completamente), ¿qué tanto cree que ayudar en su casa dificulta su proceso de aprendizaje?")

    p_family = models.IntegerField(min=0, max=15, label="13.	¿Cuántas personas conforman el hogar donde vive actualmente, incluido usted? ")

    p_rooms = models.IntegerField(min=0, max=10, label="14.	En total, ¿en cuántos cuartos duermen las personas de su hogar?")

    p_poverty = models.IntegerField(
    choices=[
        [1, 'Muy buenas'],
        [2, 'Buenas'],
        [3, 'Regulares'],
        [4, 'Malas'],
    ], label="15. ¿Cómo describiría las condiciones económicas de su hogar?")

    p_migration = models.IntegerField(
    choices=[
        [1, 'No.'],
        [2, 'Sí, por trabajo.'],
        [3, 'Sí, por educación.'],
        [4, 'Sí, por salud.'],
        [5, 'Sí, por las condiciones de seguridad.'],
        [6, 'Sí, otra razón.'],
    ], label="16. El siguiente año, ¿cree que se va a ir a vivir a otro municipio?")

    p_health = models.IntegerField(
    choices=[
        [1,'Subsidiado'],
        [2,'Contributivo (incluye regímenes especiales)']
    ], label="17. ¿A qué régimen de seguridad social en salud pertenece?")

    p_pension2 = models.IntegerField(
    choices=[
        [1,'Aportando en un fondo de pensiones obligatorias'],
        [2,'Aportando en un fondo de pensiones voluntarias (por ejemplo, BEPS)'],
        [3,'Ahorrando'],
        [4,'Haciendo inversiones'],
        [5,'Pagando un seguro por su cuenta'],
        [6,'Preparando a los hijos para que puedan ayudarlos en su vejez'],
        [7,'Nada'],
    ], label="18. ¿Qué están haciendo (hicieron) sus padres para mantenerse económicamente en la vejez?")

    ocu_mother = models.IntegerField(
    choices=[
        [1,'Empleada con cargo como director o gerente general'],
        [2,'Empleada de nivel auxiliar o administrativo'],
        [3,'Empleada de nivel directivo'],
        [4,'Empleada de nivel técnico o profesional'],
        [5,'Empleada obrera u operaria'],
        [6,'Empresaria'],
        [7,'Pequeña empresaria'],
        [8,'Profesional independiente'],
        [9,'Trabajadora por cuenta propia'],
        [10,'Hogar'],
        [11,'Pensionada'],
        [12,'Desempleada'],
        [13,'Otra actividad u ocupación'],
    ], label="19. Ocupación u oficio de la madre")

    ocu_father = models.IntegerField(
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
    ], label="20. Ocupación u oficio del padre")


    icfes_m1 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_m2 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_l1 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_l2 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_n1 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_n2 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_s1 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")
    icfes_s2 = models.StringField(choices=['A', 'B', 'C', 'D'], widget=widgets.RadioSelectHorizontal, label="Seleccione solo UNA respuesta:")

    p_risk = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="¿Qué tan dispuesto (a) está o no está usted a tomar riesgos?"
                                       )
    p_time = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="¿Qué tan dispuesto está a renunciar a algo que es beneficioso para usted en este momento a fin de obtener mayores beneficios en el futuro?"
                                       )
    p_time2 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="¿Qué tan dispuesto está a posponer las tareas, incluso cuando sabe que sería mejor hacerlas de inmediato?"
                                       )



    












