from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class intro_01(Page):
    def vars_for_template(self):
        return {
            'graphType': self.player.participant.vars['graphType'],
        }

# intro
class graph_01(Page):
    form_model = "player"
    form_fields = ["test_01_number", "test_01_answer", "test_01_time"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'max_y': max(Constants.inv_a),
                'min_y': min(Constants.inv_a),
                'time_steps': Constants.time_steps,
                'money_example': Constants.money_example,
                'answers': Constants.answer_1
                }

class graph_02(Page):
    form_model = "player"
    form_fields = [ "test_02_number", "test_02_answer", "test_02_time", 
                    "test_03_number", "test_03_answer", "test_03_time", 
                    "test_04_number", "test_04_answer", "test_04_time",
                    "test_05_number_a", "test_05_answer_a", 
                    "test_05_number_b", "test_05_answer_b", 
                    "test_05_time"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'time_steps': Constants.time_steps,
                'money_example': Constants.money_example,
                'graphType': self.player.participant.vars['graphType']
                }

class instruc_01(Page):
    pass


class intro_02(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'max_y': max(Constants.inv_a),
                'min_y': min(Constants.inv_a),
                'investment_max': Constants.investment_max
                }


class graph_03(Page):
    form_model = "player"
    form_fields = [ "test_06_number_a", "test_06_answer_a", 
                    "test_06_number_b", "test_06_answer_b", 
                    "test_06_time"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType'],
                'investment_max': Constants.investment_max
                }

class instruc_02(Page):
    pass


class intro_03(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'max_y': max(Constants.inv_a),
                'min_y': min(Constants.inv_a),
                'investment_max': Constants.investment_max
                }

# inicia a mostrar las cartas
class graph_04(Page):
    form_model = "player"
    form_fields = [ "test_07_number_a", 
                    "test_07_number_b",
                    "test_07_time", 
                    "test_07_mistakes"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType'],
                'investment_max': Constants.investment_max
                }


page_sequence = [
    intro_01, 
    graph_01, 
    graph_02, 
    instruc_01,
    intro_02,
    graph_03,
    instruc_02,
    intro_03,
    graph_04
    ]
