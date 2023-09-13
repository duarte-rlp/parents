from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
    
class questions(Page):
    form_model = 'player'
    form_fields = ['p_age', 'p_sex', 'p_married', 'p_family', 'p_children', 'p_workers', 'p_educ', 'p_job', 'p_inc', 'p_inc1', 'p_expenses']
    def is_displayed(self):
        return self.round_number == 1

class risk(Page):
    form_model = 'player'
    form_fields = ['p_risk', 'p_risk1', 'p_returns', 'p_risk2', 'p_loss', 'p_insurance', 'p_patience']
    def is_displayed(self):
        return self.round_number == 1

class agro(Page):
    form_model = 'player'
    form_fields = ['p_hectareas', 'p_farminc', 'p_crops', 'p_crops1', 'p_crops3', 'p_savings', 'p_climate', 'p_events', 'p_measures']
    def is_displayed(self):
        return self.round_number == 1

page_sequence = [questions, risk, agro]
