from Core.UI.Elements.Abstract.Label import Label
from Utils.Constant import Color


class Score(Label):

    _position = (5, 5)
    _prefix = 'Score: '

    def add_score(self, score):
        self._value += score


