from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class questions1(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        return self.round_number == 1
 

class questions2(Page):
    form_model = 'player'
    form_fields = ['p_sex', 'p_age', 'p_educ', 'p_job', 'p_inc', 'p_inc1', 'p_married', 'p_children', 'ocu_father'] 
    def is_displayed(self):
        return self.round_number == 1


class time(Page):
    form_model = 'player'
    form_fields = ['p_risk','p_time','p_time2']
    def is_displayed(self):
        return self.round_number == 1


class thanks(Page):
    pass

page_sequence = [occupation2, saber11, education, selfefficacy, barriers, income, instructions_transitions]

#

transitions = [transition1, transition2, transition3]
random.shuffle(transitions)

for t in transitions:
    page_sequence.append(t)

for t in [questions1, thanks]:
    page_sequence.append(t)

