from Core.UI.Elements.IntLabel import IntLabel


class UserInterface:

    _elements = {}
    _panels = []

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
            'score': IntLabel((5, 5), 'Score :'),
            'wallet': IntLabel((5, 25), '$ '),
        })

    def add_element(self, element_name, element):
        self._elements.update({
                element_name: element,
        })
        self._panels.append(element_name)

    def remove_panel(self):
        for panel_name in self._panels:
            del self._elements[panel_name]

        self._panels.clear()

