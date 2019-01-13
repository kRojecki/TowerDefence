import copy


class Collection:

    _elements = None

    def __init__(self, elements=[]):
        self._elements = copy.deepcopy(elements)

    def append(self, element):
        self._elements.append(element)

    def remove(self, element):
        self._elements.remove(element)

    def get(self, index):
        return self._elements[index]

    def update(self):
        for element in self._elements:
            element.update()

    def draw(self, screen):
        for element in self._elements:
            element.draw(screen)

    def __len__(self):
        return len(self._elements)

    def get_elements(self):
        for element in self._elements:
            yield element



