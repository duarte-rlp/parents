from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class intro_math(Page):
#    """
#    Show the player the rules, and allow them to start the task
#    """
    def is_displayed(self):
        return self.round_number == 1    


class p1(Page):
    form_model = "player"
    form_fields = ["p1"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
        }

class p2(Page):
    form_model = "player"
    form_fields = ["p2"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
        }

class p3(Page):
    form_model = "player"
    form_fields = ["p3"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
        }

class p4(Page):
    form_model = "player"
    form_fields = ["p4"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
        }

class p5(Page):
    form_model = "player"
    form_fields = ["p5"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
        }

class p6(Page):
    form_model = "player"
    form_fields = ["p6"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
        }

class p7(Page):
    form_model = "player"
    form_fields = ["p7"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
        }

class p8(Page):
    form_model = "player"
    form_fields = ["p8"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
        }

class p9(Page):
    form_model = "player"
    form_fields = ["p9"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
        }

class p10(Page):
    form_model = "player"
    form_fields = ["p10"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
        }


class Results(Page):
    """
    Show the results of the effort task after the player has finished
    """

    # Only show this on the last round
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

#    def vars_for_template(self):
#        return{
#            "current_score": self.player.participant.vars['effort_score']
#        }


page_sequence = [intro_math]

questions = [
    p1,
    p2,
    p3,
    p4,
    p5,
    p6,
    p7,
    p8,
    p9,
    p10
]

random.shuffle(questions)

for p in questions:
    page_sequence.append(p)

page_sequence.append(Results)
