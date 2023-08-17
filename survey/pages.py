from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class climate(Page):
    form_model = 'player'
    form_fields = ['p_climate1','p_climate2','p_climate3','p_climate4','p_climate5','p_climate6','p_climate7','p_climate8','p_climate9','p_climate10','p_climate11','p_climate12','p_climate13','p_climate14','p_climate15'] 
    def is_displayed(self):
        return self.round_number == 1
    
class questions(Page):
    form_model = 'player'
    form_fields = ['p_age', 'p_sex', 'p_married', 'p_family', 'p_children', 'p_workers', 'p_educ', 'p_job', 'p_inc', 'p_inc1', 'p_expenses', 'p_dexpenses', 'p_group', 'p_insurance', 'p_savings', 'p_pension', 'p_events', 'p_climate', 'p_season', 'p_precautions' ]
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [climate, questions]
