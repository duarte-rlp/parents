from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class instructions(Page):
    pass


class couple(Page):
    form_model = 'player'
    form_fields = ['option', 'time_choice', 'choices']


page_sequence = [instructions, couple]
