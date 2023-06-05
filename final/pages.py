from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import otree

import random
import pandas as pd

# Problema de -50%
problem_01 = pd.DataFrame({
        'Col_A': [
            20,
            20,
            20,
            20,
            -9,
            -9,
            -9,
            -9
            ],
        'Col_B': [
            -10,
            -10,
            -10,
            19,
            19,
            19,
            19,
            -10
            ]
        }, index = [1, 2, 3, 4, 5, 6, 7, 8])

# Problema de 0%
problem_02 = pd.DataFrame({
        'Col_A': [
            20,
            20,
            20,
            20,
            -9,
            -9,
            -9,
            -9
            ],
        'Col_B': [
            -10,
            -10,
            19,
            19,
            19,
            19,
            -10,
            -10
            ]
        }, index = [1, 2, 3, 4, 5, 6, 7, 8])

# Problema de 50%
problem_03 = pd.DataFrame({
        'Col_A': [
            20,
            20,
            20,
            20,
            -9,
            -9,
            -9,
            -9
            ],
        'Col_B': [
            -10,
            19,
            19,
            19,
            19,
            -10,
            -10,
            -10
            ]
        }, index = [1, 2, 3, 4, 5, 6, 7, 8])

class final_01(Page):
    def vars_for_template(self):
        players = self.player.participant.get_players()
        apps_in_game = {}
        names_in_game = []
        for p in players:
            name_app = p.__dict__.get('name_app')
#            if name_app == 'icl':
#                apps_in_game['icl'] = p.__dict__
#                names_in_game.append('icl')
#            elif name_app == 'icl2':
#                apps_in_game['icl2'] = p.__dict__
#                names_in_game.append('icl2')
            if name_app == 'allocations':
                apps_in_game['allocations'] = p.__dict__
                names_in_game.append('allocations')
#            elif name_app == 'choice':
#                apps_in_game['choice'] = p.__dict__
#                names_in_game.append('choice')
        random.shuffle(names_in_game)
        n_app = random.randint(0, len(names_in_game)-1)
        selected_app = apps_in_game.get(names_in_game[n_app])
        data_html = {}
        data_html['menor_pago'] = 0
        self.player.menor_pago = 0
        if selected_app.get('name_app') == 'choice':
            data_html['nombre_app'] = 'Choice'
            data_html['nombre_formal'] = 'Actividad 4'
            data_html['dado'] = random.randint(1, 6)
            data_html['moneda'] = random.randint(0, 1) # 0 -> cara | 1 -> cruz
            data_html['eleccion'] = selected_app.get('row_'+str(data_html['dado']))
            if data_html['eleccion'] == 0:
                self.player.pago_total = 0 # colocar aquí el pago que si decide no tirar moneda -> Bogliacino, F., & Montealegre, F. (2020). Do negative economic shocks affect cognitive function, adherence to social norms and loss aversion?. 
                self.player.pago_calculo = self.player.pago_total
                data_html['pago_calculo'] = self.player.pago_total
            else:
                if data_html['moneda'] == 0:
                    self.player.pago_total = ((data_html['dado'] + 1) * -10000) 
                else:
                    self.player.pago_total = 60000
                self.player.pago_calculo = self.player.pago_total
                data_html['pago_calculo'] = self.player.pago_total
                if self.player.pago_total < 20000:
                    self.player.pago_total = 20000
                    data_html['menor_pago'] = 1
                    self.player.menor_pago = 1
            data_html['pago_total'] = self.player.pago_total

        elif selected_app.get('name_app') == 'allocations':
            data_html['nombre_app'] = 'Allocations'
            data_html['nombre_formal'] = 'Actividad 2'
            data_html['n_problema'] = random.randint(1, 3)
            data_html['tipo_problema'] = selected_app.get('problem_0'+str(data_html['n_problema'])+'_type')
            data_html['n_escenario'] = random.randint(1, 8)
            data_html['inversion_a'] = selected_app.get('problem_0'+str(data_html['n_problema'])+'_inv_a_slider')
            data_html['inversion_b'] = 100000 - selected_app.get('problem_0'+str(data_html['n_problema'])+'_inv_a_slider')
            data_html['order_col_a'] = selected_app.get('problem_0'+str(data_html['n_problema'])+'_order_a')
            data_html['order_col_b'] = selected_app.get('problem_0'+str(data_html['n_problema'])+'_order_b')
            data_html['inv_a'] = selected_app.get('problem_0'+str(data_html['n_problema'])+'_inv_a')

            if (data_html['tipo_problema'] == '-50%'):
                temp_selected_problem = problem_01.copy()
                col_a = 1
            elif (data_html['tipo_problema'] == '0%'):
                temp_selected_problem = problem_02.copy()
            elif (data_html['tipo_problema'] == '+50%'):
                temp_selected_problem = problem_03.copy()

            if (data_html['order_col_a'] == 'Decreasing'):
                order_col_a = 0
            else:
                order_col_a = 1
            if (data_html['order_col_b'] == 'Decreasing'):
                order_col_b = 0
            else:
                order_col_b = 1
            if (data_html['inv_a'] == 'Col_A'):
                inv_a = 1
            else:
                inv_a = 0
            temp_selected_problem = temp_selected_problem.sort_values(['Col_A', 'Col_B'], ascending = [order_col_a, order_col_b], ignore_index=True)
            if (inv_a == 1):
                selected_problem = pd.DataFrame({
                'AssetA': temp_selected_problem['Col_A'],
                'AssetB': temp_selected_problem['Col_B']
                })
            else:
                selected_problem = pd.DataFrame({
                'AssetA': temp_selected_problem['Col_B'],
                'AssetB': temp_selected_problem['Col_A']
                })

            data_html['retorno_a'] = selected_problem.iloc[data_html['n_escenario']-1]['AssetA']
            data_html['retorno_b'] = selected_problem.iloc[data_html['n_escenario']-1]['AssetB']
            self.player.pago_total = int(((data_html['retorno_a'] * data_html['inversion_a']) + (data_html['retorno_b'] * data_html['inversion_b']))/100)
            data_html['calc1'] = int((data_html['retorno_a'] * data_html['inversion_a'])/100)
            data_html['calc2'] = int((data_html['retorno_b'] * data_html['inversion_b'])/100)
            data_html['pago_calculo'] = self.player.pago_total
            self.player.pago_calculo = self.player.pago_total
            if self.player.pago_total < 20000:
                self.player.pago_total = 20000
                data_html['menor_pago'] = 1
                self.player.menor_pago = 1
            data_html['pago_total'] = self.player.pago_total
        elif selected_app.get('name_app') == 'icl':
            data_html['nombre_app'] = 'ICL1'
            data_html['nombre_formal'] = 'Actividad 1'
            data_html['pago_total'] = int(str(self.participant.vars["icl_pago"]*100).split(",")[0])
            data_html['pago_calculo'] = self.player.pago_total
            self.player.pago_calculo = self.player.pago_total
            if self.player.pago_total < 20000:
                self.player.pago_total = 20000
                data_html['menor_pago'] = 1
                self.player.menor_pago = 1
            data_html['pago_total'] = self.player.pago_total
        elif selected_app.get('name_app') == 'icl2':
            data_html['nombre_app'] = 'ICL2'
            data_html['nombre_formal'] = 'Actividad 3'
            data_html['pago_total'] = int(str(self.participant.vars["icl_pago2"]*100).split(",")[0])
            data_html['pago_calculo'] = self.player.pago_total
            self.player.pago_calculo = self.player.pago_total
            if self.player.pago_total < 20000:
                self.player.pago_total = 20000
                data_html['menor_pago'] = 1
                self.player.menor_pago = 1
            data_html['pago_total'] = self.player.pago_total
        return {
            'data': data_html
        }

class results(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1
       
    def vars_for_template(self): 
        return {
            "identificador" : self.participant.vars['identificador'],
            "pago_total" : self.player.pago_total
        }



page_sequence = [final_01, results]
