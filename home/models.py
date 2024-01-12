from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = '@hopkeinst'

doc = """
Home
"""


class Constants(BaseConstants):
    name_in_url = 'home'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def set_id_players(self):
        for j in self.get_players():
            j.set_id()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)
    identificador = models.StringField(label='Seu código é composto pela inicial do seu primeiro nome seguida da sua data de nascimento. Por exemplo, se seu nome é João e você nasceu em 1 de janeiro de 1980, seu código será J01011980. Para começar, digite seu código, escrevendo tudo em letras maiúsculas. Este código é importante para garantir a sua participação no resto da atividade e a realização do seu pagamento.')
    graphType = models.IntegerField()
    graphType_str = models.StringField()

    def set_id(self):
        self.participant.vars['identificador'] = self.in_round(1).identificador