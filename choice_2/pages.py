from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class choice(Page):
    form_model = 'player'
    form_fields = ['investment_heads', 'investment_tails', 'n_investment', 'time_choice', 'choices']
    def vars_for_template(self):
        return {
            'investment_heads': Constants.investment_heads,
            'investment_tails': Constants.investment_tails,
        }
    def before_next_page(self):
        self.player.coin_toss = random.choice(['heads', 'tails'])
        if self.player.coin_toss == 'heads':
            self.player.payoff_amount_app = self.player.investment_heads
        else:
            self.player.payoff_amount_app = self.player.investment_tails

class instructions(Page):
    pass


page_sequence = [instructions, choice]
