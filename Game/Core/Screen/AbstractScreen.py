class AbstractScreen:

    configuration = 0

    def __init__(self, configuration):
        self.configuration = configuration

    def init(self):
        pass

    def update(self, surface):
        pass