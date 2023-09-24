from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import otree

import random
import pandas as pd

data_html = {}
data_html['is_menor_pago'] = 0

class final_01(Page):
    def vars_for_template(self):
        data = self.player.data_html[1:-1]
        dict_data = {}
        for k in data.split(', '):
            d = k.split(': ')
            if "'" in d[1]:
                dict_data[d[0][1:-1]] = d[1][1:-1]
            else:
                dict_data[d[0][1:-1]] = int(d[1])
        return {
            'data': dict_data
        }

class results(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1
       
    def vars_for_template(self): 
        data = self.player.data_html[1:-1]
        dict_data = {}
        for k in data.split(', '):
            d = k.split(': ')
            if "'" in d[1]:
                dict_data[d[0][1:-1]] = d[1][1:-1]
            else:
                dict_data[d[0][1:-1]] = int(d[1])
        return {
            "identificador" : self.participant.vars['identificador'],
            "pago_total" : dict_data.get('pago_real')
        }


class calc(Page):
    def before_next_page(self):
        players = self.player.participant.get_players()
        apps_in_game = {}
        names_in_game = []
        for p in players:
            name_app = p.__dict__.get('name_app')
            if name_app != None:
                apps_in_game[name_app] = p.__dict__
                names_in_game.append(name_app)
        selected_app = random.choice(names_in_game)
        self.player.activity_pay = selected_app
        data_html['nombre_formal'] = apps_in_game[selected_app].get('name_app_2_user')
        data_html['n_app'] = apps_in_game[selected_app].get('name_app_n')
        data_html['nombre_app'] = apps_in_game[selected_app].get('name_app')
        data_html['payoff_amount_app'] = apps_in_game[selected_app].get('payoff_amount_app')
        data_html['pago_base'] = self.player.pago_base
        self.player.pago_calculo = data_html['payoff_amount_app']
        if selected_app == 'choice_2':
            data_html['n_investment'] = apps_in_game[selected_app].get('n_investment')
            data_html['coin_toss'] = apps_in_game[selected_app].get('coin_toss')
        elif selected_app == 'allocations':
            data_html['n_problem'] = apps_in_game[selected_app].get('n_problem')
            data_html['n_scene'] = apps_in_game[selected_app].get('n_scene')
            data_html['per_investment_1'] = apps_in_game[selected_app].get('per_investment_1')
            data_html['per_investment_2'] = apps_in_game[selected_app].get('per_investment_2')
            data_html['val_invesment_1'] = apps_in_game[selected_app].get('val_invesment_1')
            data_html['val_invesment_2'] = apps_in_game[selected_app].get('val_invesment_2')
            data_html['amount_invesment_1'] = apps_in_game[selected_app].get('amount_invesment_1')
            data_html['amount_invesment_2'] = apps_in_game[selected_app].get('amount_invesment_2')
        elif selected_app == 'real':
            data_html['n_scene'] = apps_in_game[selected_app].get('n_scene')
            data_html['has_1'] = apps_in_game[selected_app].get('has_cultivo_1')
            data_html['has_2'] = apps_in_game[selected_app].get('has_cultivo_2')
            data_html['amount_cultivo_1'] = apps_in_game[selected_app].get('amount_cultivo_1')
            data_html['amount_cultivo_2'] = apps_in_game[selected_app].get('amount_cultivo_2')
        elif selected_app == 'choice':
            data_html['n_investment'] = apps_in_game[selected_app].get('n_investment')
            data_html['coin_toss'] = apps_in_game[selected_app].get('coin_toss')
            data_html['eleccion'] = apps_in_game[selected_app].get('row_'+str(data_html['n_investment']))
        data_html['pago_calculo'] = self.player.pago_calculo
        if (self.player.pago_calculo + self.player.pago_base) < self.player.pago_minimo:
            self.player.is_menor_pago = 1
            data_html['is_menor_pago'] = 1
            self.player.pago_real = self.player.pago_minimo
        else:
            self.player.pago_real = self.player.pago_calculo + self.player.pago_base
        data_html['pago_real'] = self.player.pago_real
        self.player.data_html = str(data_html)



page_sequence = [calc, final_01, results]
