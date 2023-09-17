from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random
import pandas as pd

class instruc_01(Page):
    def before_next_page(self):
        # 1. Order asc or desc
        self.player.order_problem_01_a = random.randint(0, 1)
        self.player.order_problem_01_b = random.randint(0, 1)
        self.player.order_problem_02_a = random.randint(0, 1)
        self.player.order_problem_02_b = random.randint(0, 1)
        self.player.order_problem_03_a = random.randint(0, 1)
        self.player.order_problem_03_b = random.randint(0, 1)
        self.player.order_problem_04_a = random.randint(0, 1)
        self.player.order_problem_04_b = random.randint(0, 1)

        p01_temp = Constants.problem_01.copy()
        p01_temp = p01_temp.sort_values(['Col_A', 'Col_B'], ascending = [self.player.order_problem_01_a, self.player.order_problem_01_b])
        p02_temp = Constants.problem_02.copy()
        p02_temp = p02_temp.sort_values(['Col_A', 'Col_B'], ascending = [self.player.order_problem_02_a, self.player.order_problem_02_b])
        p03_temp = Constants.problem_03.copy()
        p03_temp = p03_temp.sort_values(['Col_A', 'Col_B'], ascending = [self.player.order_problem_03_a, self.player.order_problem_03_b])
        p04_temp = Constants.problem_04.copy()
        p04_temp = p04_temp.sort_values(['Col_A', 'Col_B'], ascending = [self.player.order_problem_04_a, self.player.order_problem_04_b])

        # 2. Asset A: 1 -> Col_A | 0 -> Col_B
        self.player.assetA_problem_01 = random.randint(0, 1)
        self.player.assetA_problem_02 = random.randint(0, 1)
        self.player.assetA_problem_03 = random.randint(0, 1)
        self.player.assetA_problem_04 = random.randint(0, 1)

        if self.player.assetA_problem_01 == 1:
            p01 = pd.DataFrame({
                'AssetA': p01_temp['Col_A'],
                'AssetB': p01_temp['Col_B']
                })
        else: 
            p01 = pd.DataFrame({
                'AssetA': p01_temp['Col_B'],
                'AssetB': p01_temp['Col_A']
                })

        if self.player.assetA_problem_02 == 1:
            p02 = pd.DataFrame({
                'AssetA': p02_temp['Col_A'],
                'AssetB': p02_temp['Col_B']
                })
        else: 
            p02 = pd.DataFrame({
                'AssetA': p02_temp['Col_B'],
                'AssetB': p02_temp['Col_A']
                })

        if self.player.assetA_problem_03 == 1:
            p03 = pd.DataFrame({
                'AssetA': p03_temp['Col_A'],
                'AssetB': p03_temp['Col_B']
                })
        else: 
            p03 = pd.DataFrame({
                'AssetA': p03_temp['Col_B'],
                'AssetB': p03_temp['Col_A']
                })

        if self.player.assetA_problem_04 == 1:
            p04 = pd.DataFrame({
                'AssetA': p04_temp['Col_A'],
                'AssetB': p04_temp['Col_B']
                })
        else: 
            p04 = pd.DataFrame({
                'AssetA': p04_temp['Col_B'],
                'AssetB': p04_temp['Col_A']
                })

        p01.index.name = 'Scenario'
        p02.index.name = 'Scenario'
        p03.index.name = 'Scenario'
        p04.index.name = 'Scenario'

        n_order_problems = Constants.n_problems.copy()
        random.shuffle(n_order_problems)

        self.player.participant.vars['order_problems'] = []
        self.player.participant.vars['name_order_problems'] = ""
        self.player.n_order_problems = str(n_order_problems)
        problems_temp = [p01, p02, p03, p04]
        problems = []
        for i in n_order_problems:
            self.player.participant.vars['order_problems'].append(Constants.problems[i])
            self.player.participant.vars['name_order_problems'] += Constants.name_problems[i]
            problems.append(problems_temp[i])
            self.player.participant.vars['name_order_problems'] += ', '
        self.player.name_order_problems = self.player.participant.vars['name_order_problems']
        self.player.participant.vars['problems'] = problems

    def vars_for_template(self):
        return {
            'graphType': self.player.participant.vars['graphType']
        }

class instruc_02(Page):
    def vars_for_template(self):
        return {
                'order_problems': self.player.name_order_problems,
                'n_order_problems': self.player.n_order_problems.strip('][').split(', '),
                'order_problem_01_a': self.player.order_problem_01_a,
                'order_problem_01_b': self.player.order_problem_01_b,
                'order_problem_02_a': self.player.order_problem_02_a,
                'order_problem_02_b': self.player.order_problem_02_b,
                'order_problem_03_a': self.player.order_problem_03_a,
                'order_problem_03_b': self.player.order_problem_03_b,
                'order_problem_04_a': self.player.order_problem_04_a,
                'order_problem_04_b': self.player.order_problem_04_b,
                'assetA_problem_01': self.player.assetA_problem_01,
                'assetA_problem_02': self.player.assetA_problem_02,
                'assetA_problem_03': self.player.assetA_problem_03,
                'assetA_problem_04': self.player.assetA_problem_04,
                'problems': self.player.participant.vars['problems'],
                'n_problems': list(range(len(self.player.participant.vars['problems'])))
                }

class graph_01(Page):
    form_model = "player"
    form_fields = ["problem_01_btnSelected", "problem_01_btnTime", "problem_01_sliderSelected", "problem_01_sliderTime", "problem_01_sliderInv_a", "problem_01_invCntMistakers", "problem_01_invMistakes", "problem_01_invTime", "problem_01_invVal_a", "problem_01_invVal_b"]
    def vars_for_template(self):
        orden = self.player.n_order_problems.strip('][').split(', ')
        if orden[0] == '0':
            self.player.problem_01_type = "-50%"
            if self.player.assetA_problem_01 == 0:
                self.player.problem_01_inv_a = 'Col_B'
            else:
                self.player.problem_01_inv_a = 'Col_A'
            if self.player.order_problem_01_a == 0:
                self.player.problem_01_order_a = 'Decreasing'
            else:
                self.player.problem_01_order_a = 'Increasing'
            if self.player.order_problem_01_b == 0:
                self.player.problem_01_order_b = 'Decreasing'
            else:
                self.player.problem_01_order_b = 'Increasing'
        elif orden[0] == '1': 
            self.player.problem_01_type = "0%"
            if self.player.assetA_problem_02 == 0:
                self.player.problem_01_inv_a = 'Col_B'
            else:
                self.player.problem_01_inv_a = 'Col_A'
            if self.player.order_problem_02_a == 0:
                self.player.problem_01_order_a = 'Decreasing'
            else:
                self.player.problem_01_order_a = 'Increasing'
            if self.player.order_problem_02_b == 0:
                self.player.problem_01_order_b = 'Decreasing'
            else:
                self.player.problem_01_order_b = 'Increasing'
        elif orden[0] == '2': 
            self.player.problem_01_type = "+50%"
            if self.player.assetA_problem_03 == 0:
                self.player.problem_01_inv_a = 'Col_B'
            else:
                self.player.problem_01_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_01_order_a = 'Decreasing'
            else:
                self.player.problem_01_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_01_order_b = 'Decreasing'
            else:
                self.player.problem_01_order_b = 'Increasing'
        elif orden[0] == '3':
            self.player.problem_01_type = "+100%"
            if self.player.assetA_problem_04 == 0:
                self.player.problem_01_inv_a = 'Col_B'
            else:
                self.player.problem_01_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_01_order_a = 'Decreasing'
            else:
                self.player.problem_01_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_01_order_b = 'Decreasing'
            else:
                self.player.problem_01_order_b = 'Increasing'
        return {
                'n_problem': 1,
                'data_a': list(self.player.participant.vars['problems'][0]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][0]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][0]['AssetA']) + list(self.player.participant.vars['problems'][0]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][0]['AssetA']) + list(self.player.participant.vars['problems'][0]['AssetB']))
                }

class graph_01_a(Page):
    form_model = "player"
    form_fields = ["problem_01_btnSelected", "problem_01_btnTime"]
    def vars_for_template(self):
        return {
                'n_problem': 1,
                'data_a': list(self.player.participant.vars['problems'][0]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][0]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][0]['AssetA']) + list(self.player.participant.vars['problems'][0]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][0]['AssetA']) + list(self.player.participant.vars['problems'][0]['AssetB']))
                }

class graph_01_b(Page):
    form_model = "player"
    form_fields = ["problem_01_sliderSelected", "problem_01_sliderTime", "problem_01_sliderInv_a"]
    def vars_for_template(self):
        return {
                'n_problem': 1,
                'data_a': list(self.player.participant.vars['problems'][0]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][0]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][0]['AssetA']) + list(self.player.participant.vars['problems'][0]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][0]['AssetA']) + list(self.player.participant.vars['problems'][0]['AssetB']))
                }

class graph_01_c(Page):
    form_model = "player"
    form_fields = ["problem_01_invCntMistakers", "problem_01_invMistakes", "problem_01_invTime", "problem_01_invVal_a", "problem_01_invVal_b"]
    def vars_for_template(self):
        return {
                'n_problem': 1,
                'data_a': list(self.player.participant.vars['problems'][0]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][0]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][0]['AssetA']) + list(self.player.participant.vars['problems'][0]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][0]['AssetA']) + list(self.player.participant.vars['problems'][0]['AssetB']))
                }

class questions_problem_01(Page):
    form_model = "player"
    form_fields = ["problem_01_return_b", "problem_01_expect_return_b", "problem_01_probability_b", 'problem_01_risk', 'problem_01_insurance']
    def vars_for_template(self):
        orden = self.player.n_order_problems.strip('][').split(', ')
        if orden[0] == '0':
            self.player.problem_01_type = "-50%"
            if self.player.assetA_problem_01 == 0:
                self.player.problem_01_inv_a = 'Col_B'
            else:
                self.player.problem_01_inv_a = 'Col_A'
            if self.player.order_problem_01_a == 0:
                self.player.problem_01_order_a = 'Decreasing'
            else:
                self.player.problem_01_order_a = 'Increasing'
            if self.player.order_problem_01_b == 0:
                self.player.problem_01_order_b = 'Decreasing'
            else:
                self.player.problem_01_order_b = 'Increasing'
        elif orden[0] == '1': 
            self.player.problem_01_type = "0%"
            if self.player.assetA_problem_02 == 0:
                self.player.problem_01_inv_a = 'Col_B'
            else:
                self.player.problem_01_inv_a = 'Col_A'
            if self.player.order_problem_02_a == 0:
                self.player.problem_01_order_a = 'Decreasing'
            else:
                self.player.problem_01_order_a = 'Increasing'
            if self.player.order_problem_02_b == 0:
                self.player.problem_01_order_b = 'Decreasing'
            else:
                self.player.problem_01_order_b = 'Increasing'
        elif orden[0] == '2': 
            self.player.problem_01_type = "+50%"
            if self.player.assetA_problem_03 == 0:
                self.player.problem_01_inv_a = 'Col_B'
            else:
                self.player.problem_01_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_01_order_a = 'Decreasing'
            else:
                self.player.problem_01_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_01_order_b = 'Decreasing'
            else:
                self.player.problem_01_order_b = 'Increasing'
        elif orden[0] == '3':
            self.player.problem_01_type = "+100%"
            if self.player.assetA_problem_04 == 0:
                self.player.problem_01_inv_a = 'Col_B'
            else:
                self.player.problem_01_inv_a = 'Col_A'
            if self.player.order_problem_04_a == 0:
                self.player.problem_01_order_a = 'Decreasing'
            else:
                self.player.problem_01_order_a = 'Increasing'
            if self.player.order_problem_04_b == 0:
                self.player.problem_01_order_b = 'Decreasing'
            else:
                self.player.problem_01_order_b = 'Increasing'
        return {
                'n_problem': 1,
                'assetA_order': self.player.problem_01_order_a,
                'assetB_order': self.player.problem_01_order_b,
                'assetA': self.player.problem_01_inv_a,
                'data_a': list(self.player.participant.vars['problems'][0]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][0]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][0]['AssetA']) + list(self.player.participant.vars['problems'][0]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][0]['AssetA']) + list(self.player.participant.vars['problems'][0]['AssetB']))
                }

class graph_02(Page):
    form_model = "player"
    form_fields = ["problem_02_btnSelected", "problem_02_btnTime", "problem_02_sliderSelected", "problem_02_sliderTime", "problem_02_sliderInv_a", "problem_02_invCntMistakers", "problem_02_invMistakes", "problem_02_invTime", "problem_02_invVal_a", "problem_02_invVal_b"]
    def vars_for_template(self):
        orden = self.player.n_order_problems.strip('][').split(', ')
        if orden[1] == '0':
            self.player.problem_02_type = "-50%"
            if self.player.assetA_problem_01 == 0:
                self.player.problem_02_inv_a = 'Col_B'
            else:
                self.player.problem_02_inv_a = 'Col_A'
            if self.player.order_problem_01_a == 0:
                self.player.problem_02_order_a = 'Decreasing'
            else:
                self.player.problem_02_order_a = 'Increasing'
            if self.player.order_problem_01_b == 0:
                self.player.problem_02_order_b = 'Decreasing'
            else:
                self.player.problem_02_order_b = 'Increasing'
        elif orden[1] == '1': 
            self.player.problem_02_type = "0%"
            if self.player.assetA_problem_02 == 0:
                self.player.problem_02_inv_a = 'Col_B'
            else:
                self.player.problem_02_inv_a = 'Col_A'
            if self.player.order_problem_02_a == 0:
                self.player.problem_02_order_a = 'Decreasing'
            else:
                self.player.problem_02_order_a = 'Increasing'
            if self.player.order_problem_02_b == 0:
                self.player.problem_02_order_b = 'Decreasing'
            else:
                self.player.problem_02_order_b = 'Increasing'
        elif orden[1] == '2': 
            self.player.problem_02_type = "+50%"
            if self.player.assetA_problem_03 == 0:
                self.player.problem_02_inv_a = 'Col_B'
            else:
                self.player.problem_02_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_02_order_a = 'Decreasing'
            else:
                self.player.problem_02_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_02_order_b = 'Decreasing'
            else:
                self.player.problem_02_order_b = 'Increasing'
        elif orden[1] == '3':
            self.player.problem_02_type = "+100%"
            if self.player.assetA_problem_04 == 0:
                self.player.problem_02_inv_a = 'Col_B'
            else:
                self.player.problem_02_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_02_order_a = 'Decreasing'
            else:
                self.player.problem_02_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_02_order_b = 'Decreasing'
            else:
                self.player.problem_02_order_b = 'Increasing'
        return {
                'n_problem': 2,
                'data_a': list(self.player.participant.vars['problems'][1]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][1]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][1]['AssetA']) + list(self.player.participant.vars['problems'][1]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][1]['AssetA']) + list(self.player.participant.vars['problems'][1]['AssetB']))
                }

class graph_02_a(Page):
    form_model = "player"
    form_fields = ["problem_02_btnSelected", "problem_02_btnTime"]
    def vars_for_template(self):
        return {
                'n_problem': 2,
                'data_a': list(self.player.participant.vars['problems'][1]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][1]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][1]['AssetA']) + list(self.player.participant.vars['problems'][1]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][1]['AssetA']) + list(self.player.participant.vars['problems'][1]['AssetB']))
                }

class graph_02_b(Page):
    form_model = "player"
    form_fields = ["problem_02_sliderSelected", "problem_02_sliderTime", "problem_02_sliderInv_a"]
    def vars_for_template(self):
        return {
                'n_problem': 2,
                'data_a': list(self.player.participant.vars['problems'][1]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][1]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][1]['AssetA']) + list(self.player.participant.vars['problems'][1]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][1]['AssetA']) + list(self.player.participant.vars['problems'][1]['AssetB']))
                }

class graph_02_c(Page):
    form_model = "player"
    form_fields = ["problem_02_invCntMistakers", "problem_02_invMistakes", "problem_02_invTime", "problem_02_invVal_a", "problem_02_invVal_b"]
    def vars_for_template(self):
        return {
                'n_problem': 2,
                'data_a': list(self.player.participant.vars['problems'][1]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][1]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][1]['AssetA']) + list(self.player.participant.vars['problems'][1]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][1]['AssetA']) + list(self.player.participant.vars['problems'][1]['AssetB']))
                }

class questions_problem_02(Page):
    form_model = "player"
    form_fields = ["problem_02_return_b", "problem_02_expect_return_b", "problem_02_probability_b", 'problem_02_risk', 'problem_02_insurance']
    def vars_for_template(self):
        orden = self.player.n_order_problems.strip('][').split(', ')
        if orden[1] == '0':
            self.player.problem_02_type = "-50%"
            if self.player.assetA_problem_01 == 0:
                self.player.problem_02_inv_a = 'Col_B'
            else:
                self.player.problem_02_inv_a = 'Col_A'
            if self.player.order_problem_01_a == 0:
                self.player.problem_02_order_a = 'Decreasing'
            else:
                self.player.problem_02_order_a = 'Increasing'
            if self.player.order_problem_01_b == 0:
                self.player.problem_02_order_b = 'Decreasing'
            else:
                self.player.problem_02_order_b = 'Increasing'
        elif orden[1] == '1': 
            self.player.problem_02_type = "0%"
            if self.player.assetA_problem_02 == 0:
                self.player.problem_02_inv_a = 'Col_B'
            else:
                self.player.problem_02_inv_a = 'Col_A'
            if self.player.order_problem_02_a == 0:
                self.player.problem_02_order_a = 'Decreasing'
            else:
                self.player.problem_02_order_a = 'Increasing'
            if self.player.order_problem_02_b == 0:
                self.player.problem_02_order_b = 'Decreasing'
            else:
                self.player.problem_02_order_b = 'Increasing'
        elif orden[1] == '2': 
            self.player.problem_02_type = "+50%"
            if self.player.assetA_problem_03 == 0:
                self.player.problem_02_inv_a = 'Col_B'
            else:
                self.player.problem_02_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_02_order_a = 'Decreasing'
            else:
                self.player.problem_02_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_02_order_b = 'Decreasing'
            else:
                self.player.problem_02_order_b = 'Increasing'
        elif orden[1] == '3':
            self.player.problem_02_type = "+100%"
            if self.player.assetA_problem_04 == 0:
                self.player.problem_02_inv_a = 'Col_B'
            else:
                self.player.problem_02_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_02_order_a = 'Decreasing'
            else:
                self.player.problem_02_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_02_order_b = 'Decreasing'
            else:
                self.player.problem_02_order_b = 'Increasing'
        return {
                'n_problem': 2,
                'assetA_order': self.player.problem_02_order_a,
                'assetB_order': self.player.problem_02_order_b,
                'assetA': self.player.problem_02_inv_a,
                'data_a': list(self.player.participant.vars['problems'][1]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][1]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][1]['AssetA']) + list(self.player.participant.vars['problems'][1]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][1]['AssetA']) + list(self.player.participant.vars['problems'][1]['AssetB']))
                }

class graph_03(Page):
    form_model = "player"
    form_fields = ["problem_03_btnSelected", "problem_03_btnTime", "problem_03_sliderSelected", "problem_03_sliderTime", "problem_03_sliderInv_a", "problem_03_invCntMistakers", "problem_03_invMistakes", "problem_03_invTime", "problem_03_invVal_a", "problem_03_invVal_b"]
    def vars_for_template(self):
        orden = self.player.n_order_problems.strip('][').split(', ')
        if orden[2] == '0':
            self.player.problem_03_type = "-50%"
            if self.player.assetA_problem_01 == 0:
                self.player.problem_03_inv_a = 'Col_B'
            else:
                self.player.problem_03_inv_a = 'Col_A'
            if self.player.order_problem_01_a == 0:
                self.player.problem_03_order_a = 'Decreasing'
            else:
                self.player.problem_03_order_a = 'Increasing'
            if self.player.order_problem_01_b == 0:
                self.player.problem_03_order_b = 'Decreasing'
            else:
                self.player.problem_03_order_b = 'Increasing'
        elif orden[2] == '1': 
            self.player.problem_03_type = "0%"
            if self.player.assetA_problem_02 == 0:
                self.player.problem_03_inv_a = 'Col_B'
            else:
                self.player.problem_03_inv_a = 'Col_A'
            if self.player.order_problem_02_a == 0:
                self.player.problem_03_order_a = 'Decreasing'
            else:
                self.player.problem_03_order_a = 'Increasing'
            if self.player.order_problem_02_b == 0:
                self.player.problem_03_order_b = 'Decreasing'
            else:
                self.player.problem_03_order_b = 'Increasing'
        elif orden[2] == '2': 
            self.player.problem_03_type = "+50%"
            if self.player.assetA_problem_03 == 0:
                self.player.problem_03_inv_a = 'Col_B'
            else:
                self.player.problem_03_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_03_order_a = 'Decreasing'
            else:
                self.player.problem_03_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_03_order_b = 'Decreasing'
            else:
                self.player.problem_03_order_b = 'Increasing'
        elif orden[2] == '3':
            self.player.problem_03_type = "+100%"
            if self.player.assetA_problem_04 == 0:
                self.player.problem_03_inv_a = 'Col_B'
            else:
                self.player.problem_03_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_03_order_a = 'Decreasing'
            else:
                self.player.problem_03_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_03_order_b = 'Decreasing'
            else:
                self.player.problem_03_order_b = 'Increasing'
        return {
                'n_problem': 3,
                'data_a': list(self.player.participant.vars['problems'][2]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][2]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][2]['AssetA']) + list(self.player.participant.vars['problems'][2]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][2]['AssetA']) + list(self.player.participant.vars['problems'][2]['AssetB']))
                }

class graph_03_a(Page):
    form_model = "player"
    form_fields = ["problem_03_btnSelected", "problem_03_btnTime"]
    def vars_for_template(self):
        return {
                'n_problem': 3,
                'data_a': list(self.player.participant.vars['problems'][2]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][2]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][2]['AssetA']) + list(self.player.participant.vars['problems'][2]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][2]['AssetA']) + list(self.player.participant.vars['problems'][2]['AssetB']))
                }

class graph_03_b(Page):
    form_model = "player"
    form_fields = ["problem_03_sliderSelected", "problem_03_sliderTime", "problem_03_sliderInv_a"]
    def vars_for_template(self):
        return {
                'n_problem': 3,
                'data_a': list(self.player.participant.vars['problems'][2]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][2]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][2]['AssetA']) + list(self.player.participant.vars['problems'][2]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][2]['AssetA']) + list(self.player.participant.vars['problems'][2]['AssetB']))
                }

class graph_03_c(Page):
    form_model = "player"
    form_fields = ["problem_03_invCntMistakers", "problem_03_invMistakes", "problem_03_invTime", "problem_03_invVal_a", "problem_03_invVal_b"]
    def vars_for_template(self):
        return {
                'n_problem': 3,
                'data_a': list(self.player.participant.vars['problems'][2]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][2]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][2]['AssetA']) + list(self.player.participant.vars['problems'][2]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][2]['AssetA']) + list(self.player.participant.vars['problems'][2]['AssetB']))
                }

class questions_problem_03(Page):
    form_model = "player"
    form_fields = ["problem_03_return_b", "problem_03_expect_return_b", "problem_03_probability_b", 'problem_03_risk', 'problem_03_insurance']
    def vars_for_template(self):
        orden = self.player.n_order_problems.strip('][').split(', ')
        if orden[2] == '0':
            self.player.problem_03_type = "-50%"
            if self.player.assetA_problem_01 == 0:
                self.player.problem_03_inv_a = 'Col_B'
            else:
                self.player.problem_03_inv_a = 'Col_A'
            if self.player.order_problem_01_a == 0:
                self.player.problem_03_order_a = 'Decreasing'
            else:
                self.player.problem_03_order_a = 'Increasing'
            if self.player.order_problem_01_b == 0:
                self.player.problem_03_order_b = 'Decreasing'
            else:
                self.player.problem_03_order_b = 'Increasing'
        elif orden[2] == '1': 
            self.player.problem_03_type = "0%"
            if self.player.assetA_problem_02 == 0:
                self.player.problem_03_inv_a = 'Col_B'
            else:
                self.player.problem_03_inv_a = 'Col_A'
            if self.player.order_problem_02_a == 0:
                self.player.problem_03_order_a = 'Decreasing'
            else:
                self.player.problem_03_order_a = 'Increasing'
            if self.player.order_problem_02_b == 0:
                self.player.problem_03_order_b = 'Decreasing'
            else:
                self.player.problem_03_order_b = 'Increasing'
        elif orden[2] == '2': 
            self.player.problem_03_type = "+50%"
            if self.player.assetA_problem_03 == 0:
                self.player.problem_03_inv_a = 'Col_B'
            else:
                self.player.problem_03_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_03_order_a = 'Decreasing'
            else:
                self.player.problem_03_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_03_order_b = 'Decreasing'
            else:
                self.player.problem_03_order_b = 'Increasing'
        elif orden[2] == '3':
            self.player.problem_03_type = "+100%"
            if self.player.assetA_problem_04 == 0:
                self.player.problem_03_inv_a = 'Col_B'
            else:
                self.player.problem_03_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_03_order_a = 'Decreasing'
            else:
                self.player.problem_03_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_03_order_b = 'Decreasing'
            else:
                self.player.problem_03_order_b = 'Increasing'
        return {
                'n_problem': 3,
                'assetA_order': self.player.problem_03_order_a,
                'assetB_order': self.player.problem_03_order_b,
                'assetA': self.player.problem_03_inv_a,
                'data_a': list(self.player.participant.vars['problems'][2]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][2]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][2]['AssetA']) + list(self.player.participant.vars['problems'][2]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][2]['AssetA']) + list(self.player.participant.vars['problems'][2]['AssetB']))
                }

class graph_04(Page):
    form_model = "player"
    form_fields = ["problem_04_btnSelected", "problem_04_btnTime", "problem_04_sliderSelected", "problem_04_sliderTime", "problem_04_sliderInv_a", "problem_04_invCntMistakers", "problem_04_invMistakes", "problem_04_invTime", "problem_04_invVal_a", "problem_04_invVal_b"]
    def vars_for_template(self):
        orden = self.player.n_order_problems.strip('][').split(', ')
        if orden[3] == '0':
            self.player.problem_04_type = "-50%"
            if self.player.assetA_problem_01 == 0:
                self.player.problem_04_inv_a = 'Col_B'
            else:
                self.player.problem_04_inv_a = 'Col_A'
            if self.player.order_problem_01_a == 0:
                self.player.problem_04_order_a = 'Decreasing'
            else:
                self.player.problem_04_order_a = 'Increasing'
            if self.player.order_problem_01_b == 0:
                self.player.problem_04_order_b = 'Decreasing'
            else:
                self.player.problem_04_order_b = 'Increasing'
        elif orden[3] == '1': 
            self.player.problem_04_type = "0%"
            if self.player.assetA_problem_02 == 0:
                self.player.problem_04_inv_a = 'Col_B'
            else:
                self.player.problem_04_inv_a = 'Col_A'
            if self.player.order_problem_02_a == 0:
                self.player.problem_04_order_a = 'Decreasing'
            else:
                self.player.problem_04_order_a = 'Increasing'
            if self.player.order_problem_02_b == 0:
                self.player.problem_04_order_b = 'Decreasing'
            else:
                self.player.problem_04_order_b = 'Increasing'
        elif orden[3] == '2': 
            self.player.problem_04_type = "+50%"
            if self.player.assetA_problem_03 == 0:
                self.player.problem_04_inv_a = 'Col_B'
            else:
                self.player.problem_04_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_04_order_a = 'Decreasing'
            else:
                self.player.problem_04_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_04_order_b = 'Decreasing'
            else:
                self.player.problem_04_order_b = 'Increasing'
        elif orden[3] == '3':
            self.player.problem_04_type = "+100%"
            if self.player.assetA_problem_04 == 0:
                self.player.problem_04_inv_a = 'Col_B'
            else:
                self.player.problem_04_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_04_order_a = 'Decreasing'
            else:
                self.player.problem_04_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_04_order_b = 'Decreasing'
            else:
                self.player.problem_04_order_b = 'Increasing'
        return {
                'n_problem': 4,
                'data_a': list(self.player.participant.vars['problems'][3]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][3]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][3]['AssetA']) + list(self.player.participant.vars['problems'][3]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][3]['AssetA']) + list(self.player.participant.vars['problems'][3]['AssetB']))
                }


class graph_04_a(Page):
    form_model = "player"
    form_fields = ["problem_04_btnSelected", "problem_04_btnTime"]
    def vars_for_template(self):
        return {
                'n_problem': 4,
                'data_a': list(self.player.participant.vars['problems'][3]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][3]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][3]['AssetA']) + list(self.player.participant.vars['problems'][3]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][3]['AssetA']) + list(self.player.participant.vars['problems'][3]['AssetB']))
                }

class graph_04_b(Page):
    form_model = "player"
    form_fields = ["problem_04_sliderSelected", "problem_04_sliderTime", "problem_04_sliderInv_a"]
    def vars_for_template(self):
        return {
                'n_problem': 4,
                'data_a': list(self.player.participant.vars['problems'][3]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][3]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][3]['AssetA']) + list(self.player.participant.vars['problems'][3]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][3]['AssetA']) + list(self.player.participant.vars['problems'][3]['AssetB']))
                }

class graph_04_c(Page):
    form_model = "player"
    form_fields = ["problem_04_invCntMistakers", "problem_04_invMistakes", "problem_04_invTime", "problem_04_invVal_a", "problem_04_invVal_b"]
    def vars_for_template(self):
        return {
                'n_problem': 4,
                'data_a': list(self.player.participant.vars['problems'][3]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][3]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][3]['AssetA']) + list(self.player.participant.vars['problems'][3]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][3]['AssetA']) + list(self.player.participant.vars['problems'][3]['AssetB']))
                }

class questions_problem_04(Page):
    form_model = "player"
    form_fields = ["problem_04_return_b", "problem_04_expect_return_b", "problem_04_probability_b", 'problem_04_risk', 'problem_04_insurance']
    def vars_for_template(self):
        orden = self.player.n_order_problems.strip('][').split(', ')
        if orden[3] == '0':
            self.player.problem_04_type = "-50%"
            if self.player.assetA_problem_01 == 0:
                self.player.problem_04_inv_a = 'Col_B'
            else:
                self.player.problem_04_inv_a = 'Col_A'
            if self.player.order_problem_01_a == 0:
                self.player.problem_04_order_a = 'Decreasing'
            else:
                self.player.problem_04_order_a = 'Increasing'
            if self.player.order_problem_01_b == 0:
                self.player.problem_04_order_b = 'Decreasing'
            else:
                self.player.problem_04_order_b = 'Increasing'
        elif orden[3] == '1': 
            self.player.problem_04_type = "0%"
            if self.player.assetA_problem_02 == 0:
                self.player.problem_04_inv_a = 'Col_B'
            else:
                self.player.problem_04_inv_a = 'Col_A'
            if self.player.order_problem_02_a == 0:
                self.player.problem_04_order_a = 'Decreasing'
            else:
                self.player.problem_04_order_a = 'Increasing'
            if self.player.order_problem_02_b == 0:
                self.player.problem_04_order_b = 'Decreasing'
            else:
                self.player.problem_04_order_b = 'Increasing'
        elif orden[0] == '2': 
            self.player.problem_04_type = "+50%"
            if self.player.assetA_problem_03 == 0:
                self.player.problem_04_inv_a = 'Col_B'
            else:
                self.player.problem_04_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_04_order_a = 'Decreasing'
            else:
                self.player.problem_04_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_04_order_b = 'Decreasing'
            else:
                self.player.problem_04_order_b = 'Increasing'
        elif orden[0] == '3':
            self.player.problem_04_type = "+100%"
            if self.player.assetA_problem_04 == 0:
                self.player.problem_04_inv_a = 'Col_B'
            else:
                self.player.problem_04_inv_a = 'Col_A'
            if self.player.order_problem_03_a == 0:
                self.player.problem_04_order_a = 'Decreasing'
            else:
                self.player.problem_04_order_a = 'Increasing'
            if self.player.order_problem_03_b == 0:
                self.player.problem_04_order_b = 'Decreasing'
            else:
                self.player.problem_04_order_b = 'Increasing'
        return {
                'n_problem': 4,
                'assetA_order': self.player.problem_03_order_a,
                'assetB_order': self.player.problem_03_order_b,
                'assetA': self.player.problem_03_inv_a,
                'data_a': list(self.player.participant.vars['problems'][3]['AssetA']),
                'data_b': list(self.player.participant.vars['problems'][3]['AssetB']),
                'labels': Constants.inv_labels,
                'graphType': self.player.participant.vars['graphType'],
                'max_inv': Constants.max_inv,
                'max_y': max(list(self.player.participant.vars['problems'][3]['AssetA']) + list(self.player.participant.vars['problems'][3]['AssetB'])),
                'min_y': min(list(self.player.participant.vars['problems'][3]['AssetA']) + list(self.player.participant.vars['problems'][3]['AssetB']))
                }
    def before_next_page(self):
        self.player.n_problem = random.randint(1, 4) # escoger el problema
        self.player.n_scene = random.randint(1, 8) # escoger el escenario
        data_a = list(self.player.participant.vars['problems'][self.player.n_problem - 1]['AssetA'])
        data_b = list(self.player.participant.vars['problems'][self.player.n_problem - 1]['AssetB'])
        self.player.per_investment_1 = data_a[self.player.n_scene - 1]
        self.player.per_investment_2 = data_b[self.player.n_scene - 1]
        if self.player.n_problem == 1:
            self.player.amount_invesment_1 = self.player.per_investment_1 * self.player.problem_01_invVal_a
            self.player.amount_invesment_2 = self.player.per_investment_2 * self.player.problem_01_invVal_b
            self.player.val_invesment_1 = self.player.problem_01_invVal_a
            self.player.val_invesment_2 = self.player.problem_01_invVal_b
        elif self.player.n_problem == 2:
            self.player.amount_invesment_1 = self.player.per_investment_1 * self.player.problem_02_invVal_a
            self.player.amount_invesment_2 = self.player.per_investment_2 * self.player.problem_02_invVal_b
            self.player.val_invesment_1 = self.player.problem_02_invVal_a
            self.player.val_invesment_2 = self.player.problem_02_invVal_b
        elif self.player.n_problem == 3:
            self.player.amount_invesment_1 = self.player.per_investment_1 * self.player.problem_03_invVal_a
            self.player.amount_invesment_2 = self.player.per_investment_2 * self.player.problem_03_invVal_b
            self.player.val_invesment_1 = self.player.problem_03_invVal_a
            self.player.val_invesment_2 = self.player.problem_03_invVal_b
        elif self.player.n_problem == 4:
            self.player.amount_invesment_1 = self.player.per_investment_1 * self.player.problem_04_invVal_a
            self.player.amount_invesment_2 = self.player.per_investment_2 * self.player.problem_04_invVal_b
            self.player.val_invesment_1 = self.player.problem_04_invVal_a
            self.player.val_invesment_2 = self.player.problem_04_invVal_b
        self.player.amount_invesment_1 = int(self.player.amount_invesment_1/100)
        self.player.amount_invesment_2 = int(self.player.amount_invesment_2/100)
        self.player.payoff_amount_app = self.player.amount_invesment_1 + self.player.amount_invesment_2


page_sequence = [
                instruc_01, 
                #instruc_02, # retro de cómo quedan los datos ordenados
                graph_01,
                #graph_01_a, # gráfica que varía el $$ en la tabla
                #graph_01_b,
                #graph_01_c,
                questions_problem_01,
                graph_02,
                #graph_02_a,
                #graph_02_b,
                #graph_02_c,
                questions_problem_02,
                graph_03,
                #graph_03_a,
                #graph_03_b,
                #graph_03_c,
                questions_problem_03,
                graph_04,
                #graph_04_a,
                #graph_04_b,
                #graph_04_c,
                questions_problem_04,
                ]
