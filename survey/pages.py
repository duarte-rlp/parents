from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class questions1(Page):
    form_model = 'player'
    form_fields = ['p_sex', 'p_age', 'p_educ', 'p_job', 'p_inc', 'p_inc1', 'p_married', 'p_children', 'ocu_father']
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [questions1]
