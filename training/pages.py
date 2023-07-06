from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class intro_01(Page):
    pass

class intro_02(Page):
    pass

# intro
class graph_01(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

class graph_02(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

class graph_03(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

# inicia a mostrar las cartas
class graph_04(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

# pregunta 
class graph_04_question(Page):
    form_model = "player"
    form_fields = ["test_01_number", "test_01_answer"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

# respuesta correcta o incorrecta
class graph_04_feedback(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example),
                'feedback': self.player.test_01_answer
                }

class graph_05(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

class graph_06(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example[:3],
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

class graph_07(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example[:4],
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

class graph_08(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example[:5],
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

class graph_09(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example[:6],
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

class graph_10(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example[:7],
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

class graph_11(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

class graph_11_question(Page):
    form_model = "player"
    form_fields = ["test_02_number", "test_02_answer"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

class graph_11_feedback(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example),
                'feedback': self.player.test_02_answer
                }

class graph_12(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data': Constants.inv_example,
                'max_y': max(Constants.inv_example),
                'min_y': min(Constants.inv_example)
                }

# intro para múltiples gráficas
class graph_13(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

# inicia cartas
class graph_14(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class graph_15(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a[:2],
                'data_b': Constants.inv_b[:2],
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class graph_16(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a[:3],
                'data_b': Constants.inv_b[:3],
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class graph_17(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a[:4],
                'data_b': Constants.inv_b[:4],
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class graph_18(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a[:5],
                'data_b': Constants.inv_b[:5],
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class graph_19(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a[:6],
                'data_b': Constants.inv_b[:6],
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class graph_20(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a[:7],
                'data_b': Constants.inv_b[:7],
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class graph_21(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

# pregunta por cantidad de pérdidas
class graph_21_question(Page):
    form_model = "player"
    form_fields = ["test_03_A_number", "test_03_A_answer", "test_03_B_number", "test_03_B_answer"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class graph_21_feedback(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType'],
                'feedback_A': self.player.test_03_A_answer,
                'feedback_B': self.player.test_03_B_answer,
                'cnt_pos_A': len(list(filter(lambda x: (x > 0), Constants.inv_a))),
                'cnt_pos_B': len(list(filter(lambda x: (x > 0), Constants.inv_a)))
                }

class graph_22_question(Page):
    form_model = "player"
    form_fields = ["test_04_A_number", "test_04_A_answer", "test_04_B_number", "test_04_B_answer"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class graph_22_feedback(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType'],
                'feedback_A': self.player.test_04_A_answer,
                'feedback_B': self.player.test_04_B_answer,
                'cnt_neg_A': len(list(filter(lambda x: (x < 0), Constants.inv_a))),
                'cnt_neg_B': len(list(filter(lambda x: (x < 0), Constants.inv_a)))
                }

class graph_23(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class graph_24(Page):
    def vars_for_template(self):
        self.player.test_05_cardIndex = random.randint(1, 8)
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType'],
                'card_index': self.player.test_05_cardIndex
                }

class graph_24_question(Page):
    form_model = "player"
    form_fields = ["test_05_A_number", "test_05_A_answer", "test_05_B_number", "test_05_B_answer"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType'],
                'card_index': self.player.test_05_cardIndex
                }

class graph_24_feedback(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType'],
                'feedback_A': self.player.test_05_A_answer,
                'feedback_B': self.player.test_05_B_answer,
                'card_index': self.player.test_05_cardIndex,
                'val_a': Constants.inv_a[self.player.test_05_cardIndex-1],
                'val_b': Constants.inv_b[self.player.test_05_cardIndex-1]
                }

class graph_25(Page):
    form_model = "player"
    form_fields = ["test_06_cardIndex"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class instruc_01(Page):
    pass

class instruc_02(Page):
    pass

class graph_26(Page):
    form_model = "player"
    form_fields = ["slider_example"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType']
                }

class graph_27(Page):
    form_model = "player"
    form_fields = ["test_07_cardIndex"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType'],
                'inv_a': self.player.slider_example,
                'inv_b': 100000-self.player.slider_example
                }

class graph_28_question(Page):
    form_model = "player"
    form_fields = ["test_07_payment", "test_07_answer"]
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType'],
                'inv_a': self.player.slider_example,
                'inv_b': 100000-self.player.slider_example,
                'card_index': self.player.test_07_cardIndex
                }

class graph_28_feedback(Page):
    def vars_for_template(self):
        return {
                'labels': Constants.inv_labels,
                'data_a': Constants.inv_a,
                'data_b': Constants.inv_b,
                'max_y': max(Constants.inv_a + Constants.inv_b),
                'min_y': min(Constants.inv_a + Constants.inv_b),
                'graphType': self.player.participant.vars['graphType'],
                'inv_a': self.player.slider_example,
                'inv_b': 100000-self.player.slider_example,
                'card_index': self.player.test_07_cardIndex,
                'feedback': self.player.test_07_answer,
                'val_a': Constants.inv_a[self.player.test_07_cardIndex-1],
                'val_b': Constants.inv_b[self.player.test_07_cardIndex-1],
                'pay_a': (Constants.inv_a[self.player.test_07_cardIndex-1] * self.player.slider_example)/100,
                'pay_b': (Constants.inv_b[self.player.test_07_cardIndex-1] * (100000-self.player.slider_example))/100,
                'payment': ((Constants.inv_a[self.player.test_07_cardIndex-1] * self.player.slider_example)+(Constants.inv_b[self.player.test_07_cardIndex-1] * (100000-self.player.slider_example)))/100
                }



page_sequence = [
    intro_01, 
    graph_01, 
    graph_02, 
    graph_03, 
    graph_04, 
    graph_04_question, 
    graph_04_feedback, 
    graph_05,
    graph_13, 
    graph_14,
    graph_21_question, 
    graph_21_feedback, 
    graph_22_question, 
    graph_22_feedback,
    graph_23,
    graph_24,
    graph_24_question,
    graph_24_feedback,
    graph_25,
    instruc_01,
    instruc_02,
    graph_26,
    graph_27,
#    graph_28_question,
#    graph_28_feedback
    ]
