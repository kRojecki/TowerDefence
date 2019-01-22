from Core.UI.Elements.Abstract.Label import Label
from Utils.Constant import Color


class Wallet(Label):

    _position = (5, 25)
    _prefix = '$ '

    def add_funds(self, money):
        self._value += money


