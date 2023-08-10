from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from icl.config import *
import random


author = 'Felix Holzmeister'

doc = """
Staircase risk elicitation task as proposed by Falk et al. (2016), Working Paper.
"""


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):

    # initiate list of sure payoffs and implied switching row in first round
    # ------------------------------------------------------------------------------------------------------------
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['icl_sure_payoffs'] = [c(Constants.sure_payoff)]
                p.participant.vars['icl_switching_row'] = 2 ** Constants.num_choices


# ******************************************************************************************************************** #
# *** CLASS GROUP
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
# *** CLASS PLAYER
# ******************************************************************************************************************** #
class Player(BasePlayer):

    # add model fields to class player
    # ----------------------------------------------------------------------------------------------------------------
    sure_payoff = models.IntegerField()
    choice = models.StringField()
    switching_row = models.IntegerField()

    # Payoff variables 
    selected_round = models.IntegerField() # La ronda que se selecciona
    coin_toss = models.StringField() # Resultado al lanzar la moneda
    payoff_amount_app = models.IntegerField() # Total que se paga por esta app

    # set sure payoff for next choice
    # ----------------------------------------------------------------------------------------------------------------
    def set_sure_payoffs(self):

        # add current round's sure payoff to model field
        # ------------------------------------------------------------------------------------------------------------
        self.sure_payoff = int(self.participant.vars['icl_sure_payoffs'][self.round_number - 1])

        # determine sure payoff for next choice and append list of sure payoffs
        # ------------------------------------------------------------------------------------------------------------
        if not self.round_number == Constants.num_choices:

            if self.choice == 'A':
                self.participant.vars['icl_sure_payoffs'].append(
                    c(self.participant.vars['icl_sure_payoffs'][self.round_number - 1]
                    + Constants.delta / 2 ** (self.round_number - 1))
                )
            elif self.choice == 'B':
                self.participant.vars['icl_sure_payoffs'].append(
                    c(self.participant.vars['icl_sure_payoffs'][self.round_number - 1]
                    - Constants.delta / 2 ** (self.round_number - 1))
                )
            else:
                pass

    # update implied switching row each round
    # ----------------------------------------------------------------------------------------------------------------
    def update_switching_row(self):

        if self.choice == 'B':
            self.participant.vars['icl_switching_row'] -= 2 ** (Constants.num_choices - self.round_number)

        elif self.choice == 'I':
            self.participant.vars['icl_switching_row'] /= 2

    # set payoffs
    # ----------------------------------------------------------------------------------------------------------------
    def set_payoffs(self):

        current_round = self.subsession.round_number

        # set payoff if all choices have been completed or if "indifferent" was chosen
        # ------------------------------------------------------------------------------------------------------------
        if current_round == Constants.num_rounds:

            self.selected_round = random.randint(1, 5)

            print('ronda escogida:', self.selected_round)
            print('choice', self.in_round(self.selected_round).choice)

            if self.in_round(self.selected_round).choice == 'A':
                print('Rentabilidad fija: lanzar moneda')
                self.coin_toss = random.choice(['heads', 'tails'])
                if self.coin_toss == 'heads':
                    self.payoff_amount_app = 30000
                else:
                    self.payoff_amount_app = 0
            else:
                print('Rentabilidad variable, toma el pago seguro')
                self.coin_toss = '-'
                self.payoff_amount_app = self.in_round(ronda_escogida).sure_payoff
            
            print('moneda:', self.coin_toss)
            print('total a pagar:', self.payoff_amount_app)
            
