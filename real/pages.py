from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class graph_01(Page):
    form_model = 'player'
    form_fields = ['return_banano']
    def vars_for_template(self):
        return {
            'graphType': self.player.participant.vars['graphType'],
            'labels': Constants.anhos,
            'banano': Constants.banano,
            'title_1': 'Cultivo 1', #Banano
            'canha': Constants.canha,
            'title_2': 'Cultivo 2'#Caña de azucar
        }


page_sequence = [graph_01]
