from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class consent(Page):
    form_model = 'player'
    form_fields = ['consent','consent_account']

    def is_displayed(self):
        return self.round_number == 1

class intro_home(Page):
    form_model = 'player'
    form_fields = ['identificador']

    def is_displayed(self):
        return self.round_number == 1
    
    def before_next_page(self):
        self.subsession.set_id_players()
        self.player.participant.vars['graphType'] = random.randint(1, 2)
        self.player.graphType = self.player.participant.vars['graphType']

# Para al finalizar visualizar los datos almacenados por la app
class retro(Page):
    def vars_for_template(self):
        return {
            'graphType': self.player.participant.vars['graphType']
        }

page_sequence = [consent, intro_home]