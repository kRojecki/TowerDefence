class Collection:

    _elements = []

    def __init__(self, list=[]):
        self._elements = list

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
