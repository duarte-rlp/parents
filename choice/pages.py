from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class choice(Page):
    form_model = 'player'
    form_fields = ['row_1', 'row_2', 'row_3', 'row_4', 'row_5', 'row_6']


page_sequence = [choice]
