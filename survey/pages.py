from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
    
class questions(Page):
    form_model      =   'player'
    form_fields     =   [
                            'q_age', 
                            'q_gender', 
                            'q_married', 
                            'q_family', 
                            'q_children', 
                            'q_workers', 
                            'q_educ', 
                            'q_job', 
                            'q_income', 
                            'q_incomeRange',
                            'q_expenses'
                        ]
    def vars_for_template(self):
        return {
            'gender_list': Constants.gender_list,
            'married_list': Constants.married_list,
            'education_list': Constants.education_list,
            'job_list': Constants.job_list,
            'incomeRange_list': Constants.incomeRange_list,
            'expenses_list': Constants.expenses_list
        }
    def is_displayed(self):
        return self.round_number == 1

class risk(Page):
    form_model      =   'player'
    form_fields     =   [
                            'q_risk',
                            'q_riskList',
                            'q_returns',
                            'q_riskImportant',
                            'q_loss',
                            'q_insurance',
                            'q_patience'
                        ]
    def vars_for_template(self):
        return {
            'risk_list': Constants.risk_list,
            'insurance_list': Constants.insurance_list
        }
    def is_displayed(self):
        return self.round_number == 1

class agro(Page):
    form_model      =   'player'
    form_fields     =   [
                            '',
                            'p_hectareas', 
                            'p_farminc', 
                            'p_crops', 
                            'p_crops1', 
                            'p_crops3', 
                            'p_savings', 
                            'p_climate', 
                            'p_events', 
                            'p_measures'
                        ]
    def is_displayed(self):
        return self.round_number == 1

page_sequence = [questions, risk, agro]
