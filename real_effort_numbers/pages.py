from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class intro_math(Page):
#    """
#    Show the player the rules, and allow them to start the task
#    """
    def is_displayed(self):
        # Only show this on the first round
        # Need to show only to effort group participants
        # (and to add IntroLuckGroup IntroMixedGroup page) up here and in page sequence
        return self.round_number == 1


class p1(Page):
    form_model = "player"
    form_fields = ["p1", "p1_cnt_mistakes", "p1_mistakes", "p1_time"]

    def vars_for_template(self):
        return {
            'pregunta': self.round_number,
            'question': Constants.questions[0],
            'answer': Constants.answers[0],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class p2(Page):
    form_model = "player"
    form_fields = ["p2", "p2_cnt_mistakes", "p2_mistakes", "p2_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[1],
            'answer': Constants.answers[1],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class p3(Page):
    form_model = "player"
    form_fields = ["p3", "p3_cnt_mistakes", "p3_mistakes", "p3_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[2],
            'answer': Constants.answers[2],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class p4(Page):
    form_model = "player"
    form_fields = ["p4", "p4_cnt_mistakes", "p4_mistakes", "p4_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[3],
            'answer': Constants.answers[3],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class p5(Page):
    form_model = "player"
    form_fields = ["p5", "p5_cnt_mistakes", "p5_mistakes", "p5_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[4],
            'answer': Constants.answers[4],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class p6(Page):
    form_model = "player"
    form_fields = ["p6", "p6_cnt_mistakes", "p6_mistakes", "p6_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[5],
            'answer': Constants.answers[5],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class p7(Page):
    form_model = "player"
    form_fields = ["p7", "p7_cnt_mistakes", "p7_mistakes", "p7_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[6],
            'answer': Constants.answers[6],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class p8(Page):
    form_model = "player"
    form_fields = ["p8", "p8_cnt_mistakes", "p8_mistakes", "p8_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[7],
            'answer': Constants.answers[7],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class p9(Page):
    form_model = "player"
    form_fields = ["p9", "p9_cnt_mistakes", "p9_mistakes", "p9_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[8],
            'answer': Constants.answers[8],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class p10(Page):
    form_model = "player"
    form_fields = ["p10", "p10_cnt_mistakes", "p10_mistakes", "p10_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[9],
            'answer': Constants.answers[9],
            'n_question': self.player.cnt_question,
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

#page_sequence.append(Results)
