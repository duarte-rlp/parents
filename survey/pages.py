from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class questions1(Page):
    form_model = 'player'
    form_fields = ['p_vocational', 'p_preicfes', 'p_sex', 'p_age', 'p_work', 'p_hwork', 'p_wage', 'p_desertion', 'p_years' ]
    def is_displayed(self):
        return self.round_number == 1
 

class questions2(Page):
    form_model = 'player'
    form_fields = ['p_internet', 'p_tinternet', 'p_care', 'p_family', 'p_rooms', 'p_poverty', 'p_migration', 'p_health', 'p_pension2', 'ocu_mother', 'ocu_father'] 
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

for t in [instructions_icfes, icfes_m1, icfes_m2, icfes_l1, icfes_l2, icfes_s1, icfes_s2, icfes_n1, icfes_n2, time, questions1, questions2, thanks]:
    page_sequence.append(t)

