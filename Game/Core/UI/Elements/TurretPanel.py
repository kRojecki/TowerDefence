from Core.UI.Elements.Abstract.Panel import Panel
from Core.UI.Elements.SellButton import SellButton
from Core.UI.Elements.UpgradeButton import UpgradeButton


class TurretPanel(Panel):

    def __init__(self, linked_element):

        super().__init__(linked_element)

        self._elements.append(
            UpgradeButton('+', (10, 70), linked_element)
        )
        self._elements.append(
            SellButton('$', (65, 70), linked_element)
        )