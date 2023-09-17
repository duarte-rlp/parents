from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import otree

import random
import pandas as pd

data_html = {}
data_html['menor_pago'] = 0

class final_01(Page):
    form_model = 'player'
    form_fields = ['activity_pay', 'menor_pago', 'pago_calculo', 'pago_real']
    def vars_for_template(self):
        players = self.player.participant.get_players()
        apps_in_game = {}
        names_in_game = []
        for p in players:
            name_app = p.__dict__.get('name_app')
            if name_app != None:
                apps_in_game[name_app] = p.__dict__
                names_in_game.append(name_app)
        selected_app = random.choice(names_in_game)
        print('selected_app', selected_app)
        self.player.menor_pago = 0

        data_html['nombre_formal'] = apps_in_game[selected_app].get('name_app_2_user')
        data_html['n_app'] = apps_in_game[selected_app].get('name_app_n')
        data_html['nombre_app'] = apps_in_game[selected_app].get('name_app')

        print(data_html)


        return {
            'data': data_html
        }

class results(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1
       
    def vars_for_template(self): 
        return {
            "identificador" : self.participant.vars['identificador'],
            "pago_total" : data_html.get('pago_total')
        }



page_sequence = [final_01, results]
