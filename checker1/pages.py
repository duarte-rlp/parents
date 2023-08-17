from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class checker(Page):
    form_model = 'player'
    form_fields = ['cnt_mistakes', 'mistakes_checker', 'time_checker', 'response_checker']
    def vars_for_template(self):
        colors = Constants.colors_checker.copy()
        random.shuffle(colors)
        return {
                'colors': colors,
                'correct_color': Constants.correct_color
                }


page_sequence = [checker]
