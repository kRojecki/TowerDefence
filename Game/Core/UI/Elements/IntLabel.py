from Core.UI.Elements.Abstract.Label import Label
from Utils.Constant import Color


class IntLabel(Label):

    _value = 0

    def __init__(self, prefix, position, font_size=16, value=0):
        super().__init__(position, prefix, font_size)
        self._value = value

    def add(self, value):
        self._value += value

    def _get_content_to_show(self):
        return self._prefix + str(self._value)
