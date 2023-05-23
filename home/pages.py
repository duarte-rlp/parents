from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class consent(Page):
    form_model = 'player'
    form_fields = ['consent','consent_account']

    def is_displayed(self):
        return self.round_number == 1
    
class welcome_home(Page):
    def is_displayed(self):
        return self.round_number == 1

class intro_home(Page):
    form_model = 'player'
    form_fields = ['identificador']

    def is_displayed(self):
        return self.round_number == 1
    
    def before_next_page(self):
        self.subsession.set_id_players()

page_sequence = [consent, welcome_home, intro_home]