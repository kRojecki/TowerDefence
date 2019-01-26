from Core.UI.Elements.Abstract.Button import Button
from Core.UI.Elements.Abstract.Label import Label
from Core.UI.Elements.Abstract.Panel import Panel


class TurretPanel(Panel):

    def __init__(self, linked_element):
        super().__init__(linked_element)
        self._elements.append(
            Button('Upgrade', (2, 2))
        )
        self._elements.append(
            Button('Sell', (0, 30))
        )
