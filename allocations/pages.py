from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class graph_01(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

class graph_01_01(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example[:1]
                }

class graph_01_02(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example[:2]
                }
                
class graph_01_03(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example[:3]
                }
                
class graph_01_04(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example[:4]
                }
                
class graph_01_05(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example[:5]
                }
                
class graph_01_06(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example[:6]
                }

class graph_02(Page):
    def vars_for_template(self):
        return {
                'data_01': Constants.inv_a,
                'data_02': Constants.inv_b
                }

class graph_03(Page):
    def vars_for_template(self):
        return {
                'data_01': Constants.inv_a,
                'data_02': Constants.inv_b
                }


page_sequence = [graph_01, graph_01_01, graph_01_02, graph_01_03, graph_01_04, graph_01_05, graph_01_06, graph_02, graph_03]
