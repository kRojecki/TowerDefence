class Collection:

    _elements = []

    def __init__(self, list):
        self._elements = list

    def append(self, element):
        self._elements.append(element)

    def get(self, index):
        return self._elements[index]

    def update(self):
        for element in self._elements:
            element.update()

    def draw(self, screen):
        for element in self._elements:
            element.draw(screen)
