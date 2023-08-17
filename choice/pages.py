from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class choice(Page):
    form_model = 'player'
    form_fields = ['row_1', 'row_2', 'row_3', 'row_4', 'row_5', 'row_6', 'time_choice']
    def vars_for_template(self):
        return {
        'loss': Constants.loss,
        'earnings': Constants.earnings
        }
    def before_next_page(self):
        self.player.n_investment = random.randint(1, 6) # Lanzamiento de dado 
        # para escoger entre la fila 1 y la 6
        if self.player.n_investment == 1:
            if self.player.row_1 == 0: # Escogio no invertir
                self.player.coin_toss = "-"
                self.player.payoff_amount_app = 0
            else: # Si escogio invertir
                self.player.coin_toss = random.choice(['heads', 'tails']) # Lanza la moneda
                if self.player.coin_toss == 'heads': # Si cae cara
                    # Asigna la perdid
                    self.player.payoff_amount_app = Constants.loss[self.player.n_investment - 1]
                else:
                    # Si cae sello, asigna la ganancia
                    self.player.payoff_amount_app = Constants.earnings[self.player.n_investment - 1]
        elif self.player.n_investment == 2:
            if self.player.row_2 == 0:
                self.player.coin_toss = "-"
                self.player.payoff_amount_app = 0
            else: 
                self.player.coin_toss = random.choice(['heads', 'tails'])
                if self.player.coin_toss == 'heads':
                    self.player.payoff_amount_app = Constants.loss[self.player.n_investment - 1]
                else:
                    self.player.payoff_amount_app = Constants.earnings[self.player.n_investment - 1]
        elif self.player.n_investment == 3:
            if self.player.row_3 == 0:
                self.player.coin_toss = "-"
                self.player.payoff_amount_app = 0
            else: 
                self.player.coin_toss = random.choice(['heads', 'tails'])
                if self.player.coin_toss == 'heads':
                    self.player.payoff_amount_app = Constants.loss[self.player.n_investment - 1]
                else:
                    self.player.payoff_amount_app = Constants.earnings[self.player.n_investment - 1]
        elif self.player.n_investment == 4:
            if self.player.row_4 == 0:
                self.player.coin_toss = "-"
                self.player.payoff_amount_app = 0
            else: 
                self.player.coin_toss = random.choice(['heads', 'tails'])
                if self.player.coin_toss == 'heads':
                    self.player.payoff_amount_app = Constants.loss[self.player.n_investment - 1]
                else:
                    self.player.payoff_amount_app = Constants.earnings[self.player.n_investment - 1]
        elif self.player.n_investment == 5:
            if self.player.row_5 == 0:
                self.player.coin_toss = "-"
                self.player.payoff_amount_app = 0
            else: 
                self.player.coin_toss = random.choice(['heads', 'tails'])
                if self.player.coin_toss == 'heads':
                    self.player.payoff_amount_app = Constants.loss[self.player.n_investment - 1]
                else:
                    self.player.payoff_amount_app = Constants.earnings[self.player.n_investment - 1]
        elif self.player.n_investment == 6:
            if self.player.row_6 == 0:
                self.player.coin_toss = "-"
                self.player.payoff_amount_app = 0
            else: 
                self.player.coin_toss = random.choice(['heads', 'tails'])
                if self.player.coin_toss == 'heads':
                    self.player.payoff_amount_app = Constants.loss[self.player.n_investment - 1]
                else:
                    self.player.payoff_amount_app = Constants.earnings[self.player.n_investment - 1]


class instructions(Page):
    pass

page_sequence = [instructions, choice]
