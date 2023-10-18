from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class graph_01(Page):
    form_model = 'player'
    form_fields = ['has_cultivo_1', 'has_cultivo_2', 'time_cultivos_1', 'time_cultivos_2', 'time_cultivos_3', 'cnt_mistakes']
    def vars_for_template(self):
        return {
                'labels': Constants.anhos,
                'data_a': Constants.cultivo_1,
                'data_b': Constants.cultivo_2,
                'max_y': max(Constants.cultivo_1 + Constants.cultivo_2),
                'min_y': min(Constants.cultivo_1 + Constants.cultivo_2),
                'time_steps': Constants.time_steps,
                'investment_max': Constants.investment_max,
                'graphType': self.player.participant.vars['graphType']
                }
    def before_next_page(self):
        self.player.n_scene = random.randint(1, 8) # escoger el escenario
        self.player.amount_cultivo_1 = int((Constants.cultivo_1[self.player.n_scene-1] * self.player.has_cultivo_1)/10) # calcula el $$$ por el cultivo A
        self.player.amount_cultivo_2 = int((Constants.cultivo_2[self.player.n_scene-1] * self.player.has_cultivo_2)/10) # calcula el $$$ por el cultivo B
        self.player.payoff_amount_app = self.player.amount_cultivo_1 + self.player.amount_cultivo_2


class questions_graph_01(Page):
    form_model = 'player'
    form_fields = ['time_cultivos_4', 'question_1_real', 'question_2_real', 'question_3_real', 'question_4_real', 'question_5_real']
    def vars_for_template(self):
        return {
                'labels': Constants.anhos,
                'data_a': Constants.cultivo_1,
                'data_b': Constants.cultivo_2,
                'max_y': max(Constants.cultivo_1 + Constants.cultivo_2),
                'min_y': min(Constants.cultivo_1 + Constants.cultivo_2),
                'time_steps': Constants.time_steps,
                'investment_max': Constants.investment_max,
                'graphType': self.player.participant.vars['graphType']
                }


class instructions(Page):
    pass
    

page_sequence = [
                    instructions, 
                    graph_01, 
                ]
