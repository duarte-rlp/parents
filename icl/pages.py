from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


# variables for all templates
# --------------------------------------------------------------------------------------------------------------------
def vars_for_all_templates(self):
    return {
        'p_hi': "{0:.0f}".format(Constants.probability) + "%",
        'p_lo': "{0:.0f}".format(100 - Constants.probability) + "%",
        'hi':"$"+format(int(str(Constants.lottery_hi*100).split(",")[0]), ',d'),
        'lo': "$"+format(int(str(Constants.lottery_lo*100).split(",")[0]), ',d')
    }


# ******************************************************************************************************************** #
# *** CLASS INSTRUCTIONS *** #
# ******************************************************************************************************************** #
class Instructions(Page):

    # only display instruction in round 1
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == 1


# ******************************************************************************************************************** #
# *** PAGE DECISION *** #
# ******************************************************************************************************************** #
class Decision(Page):

    # only display if previous choice was not "indifferent"
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        previous_choices = [p.choice for p in self.player.in_previous_rounds()]
        return 'I' not in previous_choices

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['choice']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for progress bar
        total = Constants.num_choices
        page = self.subsession.round_number
        progress = page / total * 100

        return {
            'page':        page,
            'total':       total,
            'progress':    progress,
            'sure_payoff': "$"+format(int(str((self.participant.vars['icl_sure_payoffs'][page - 1])*100).split(",")[0]), ',d')
        }

    # set sure payoffs for next choice, payoffs, and switching row
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(self):
        self.player.set_sure_payoffs()
        self.player.update_switching_row()
        self.player.set_payoffs()
        self.player.set_ganador_pago()


# ******************************************************************************************************************** #
# *** PAGE RESULTS *** #
# ******************************************************************************************************************** #
class Results(Page):

    # skip results until last page
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # payoff information
        choice_to_pay = self.participant.vars['icl_choice_to_pay']
        option_to_pay = self.player.in_round(choice_to_pay).choice
        payoff_relevant = self.player.in_round(choice_to_pay).payoff_relevant
        sure_payoff = self.player.participant.vars['icl_sure_payoffs'][choice_to_pay - 1]

        return {
            'sure_payoff':     "$"+format(int(str(sure_payoff*100).split(",")[0]), ',d'),
            'option_to_pay':   option_to_pay,
            'payoff_relevant': payoff_relevant,
            'payoff':          "$"+format(int(str(self.player.in_round(choice_to_pay).payoff*100).split(",")[0]), ',d')
        }


# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
page_sequence = [Decision]

if Constants.instructions:
    page_sequence.insert(0, Instructions)

if Constants.results:
    page_sequence.append(Results)
