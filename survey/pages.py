from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
    
class questions(Page):
    form_model      =   "player"
    form_fields     =   [
                            "q_age", 
                            "q_gender", 
                            "q_married", 
                            "q_family", 
                            # "q_children", 
                            "q_workers", 
                            "q_educ", 
                            "q_job", 
                            "q_income", 
                            "q_incomeRange",
                            "q_expenses",
                            "q_device"
                        ]
    def vars_for_template(self):
        return {
            "gender_list": Constants.gender_list,
            "married_list": Constants.married_list,
            "education_list": Constants.education_list,
            "job_list": Constants.job_list,
            "incomeRange_list": Constants.incomeRange_list,
            "expenses_list": Constants.expenses_list,
            "devices_list": Constants.devices_list
        }
    def is_displayed(self):
        return self.round_number == 1

class risk(Page):
    form_model      =   "player"
    form_fields     =   [
                            "q_risk",
                            "q_riskList",
                            # "q_returns",
                            # "q_riskImportant",
                            # "q_loss",
                            # "q_insurance",
                            "q_patience"
                        ]
    def vars_for_template(self):
        return {
            "risk_list": Constants.risk_list #,
            # "insurance_list": Constants.insurance_list
        }
    def is_displayed(self):
        return self.round_number == 1

class agro(Page):
    form_model      =   "player"
    form_fields     =   [
                            "q_hectares",
                            "q_farminc",
                            "q_crops",
                            "q_cropTypes",
                            # "q_cropsImp_1",
                            # "q_cropsImp_2",
                            # "q_cropsImp_3",
                            # "q_cropsImp_4",
                            # "q_cropsImp_5",
                            # "q_cropsImp_6",
                            "q_cropsLoss",
                            "q_savings",
                            "q_protection_1",
                            "q_protection_2",
                            "q_protection_3" #,
                            # "q_climate",
                            # "q_events",
                            # "q_measures"

                        ]
    def vars_for_template(self):
        return {
            "hectares_list": Constants.hectares_list,
            "farminc_list": Constants.farminc_list,
            "crops_list": Constants.crops_list,
            "cropTypes_list": Constants.cropTypes_list,
            # "cropImportance_list": Constants.cropImportance_list,
            "cropsLoss_list": Constants.cropsLoss_list,
            "savings_list": Constants.savings_list,
            "protection_list": Constants.protection_list #,
            # "climate_list": Constants.climate_list,
            # "events_list": Constants.events_list,
            # "measures_list": Constants.measures_list
        }
    def is_displayed(self):
        return self.round_number == 1

page_sequence = [questions, risk, agro]
