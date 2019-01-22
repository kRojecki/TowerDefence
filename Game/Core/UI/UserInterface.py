from Core.UI.Elements.Score import Score
from Core.UI.Elements.Wallet import Wallet


class UserInterface:

    _elements = {}

    def init(self):
        self._init_elements()
        pass

    def draw(self, screen):
        for key, element in self._elements.items():
            element.draw(screen)

    def get_element(self, name):
        return self._elements.get(name)

    def _init_elements(self):
        self._elements.update({
            'score': Score(),
            'wallet': Wallet(),
        })
