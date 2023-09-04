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
    def vars_for_template(self):
        return {
            'n_questions_letters': Constants.n_questions[0],
            'n_questions_numbers': Constants.n_questions[1],
        }


class q1(Page):
    form_model = "player"
    #form_fields = ["q1", "q1_cnt_mistakes", "q1_mistakes", "q1_time"]
    form_fields = ["q1", "q1_time"]

    def vars_for_template(self):
        return {
            'pregunta': self.round_number,
            'question': Constants.questions[0],
            'answer': Constants.answers[0],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class q2(Page):
    form_model = "player"
    #form_fields = ["q2", "q2_cnt_mistakes", "q2_mistakes", "q2_time"]
    form_fields = ["q2", "q2_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[1],
            'answer': Constants.answers[1],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class q3(Page):
    form_model = "player"
    #form_fields = ["q3", "q3_cnt_mistakes", "q3_mistakes", "q3_time"]
    form_fields = ["q3", "q3_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[2],
            'answer': Constants.answers[2],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class q4(Page):
    form_model = "player"
    #form_fields = ["q4", "q4_cnt_mistakes", "q4_mistakes", "q4_time"]
    form_fields = ["q4", "q4_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[3],
            'answer': Constants.answers[3],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class q5(Page):
    form_model = "player"
    #form_fields = ["q5", "q5_cnt_mistakes", "q5_mistakes", "q5_time"]
    form_fields = ["q5", "q5_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[4],
            'answer': Constants.answers[4],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class q6(Page):
    form_model = "player"
    #form_fields = ["q6", "q6_cnt_mistakes", "q6_mistakes", "q6_time"]
    form_fields = ["q6", "q6_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[5],
            'answer': Constants.answers[5],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class q7(Page):
    form_model = "player"
    #form_fields = ["q7", "q7_cnt_mistakes", "q7_mistakes", "q7_time"]
    form_fields = ["q7", "q7_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[6],
            'answer': Constants.answers[6],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

class q8(Page):
    form_model = "player"
    #form_fields = ["q8", "q8_cnt_mistakes", "q8_mistakes", "q8_time"]
    form_fields = ["q8", "q8_time"]

    def vars_for_template(self):
        return {
            "pregunta":self.round_number,
            'question': Constants.questions[7],
            'answer': Constants.answers[7],
            'n_question': self.player.cnt_question,
        }

    def before_next_page(self):
        self.player.cnt_question += 1

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
    q1,
    q2,
    q3,
    q4,
    q5,
    q6,
    q7,
    q8
]

#random.shuffle(questions)

for p in questions:
    page_sequence.append(p)

#page_sequence.append(Results)
