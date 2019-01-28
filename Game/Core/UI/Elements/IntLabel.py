from Core.UI.Elements.Abstract.Label import Label


class IntLabel(Label):

    _value = 0

    def __init__(self, position, prefix, value=0, font_size=12):
        super().__init__(position, prefix, font_size)
        self._value = value

    def add(self, value):
        self._value += value

    def set_value(self, value):
        self._value = value

    def _get_content_to_show(self):
        return self._prefix + str(self._value)
