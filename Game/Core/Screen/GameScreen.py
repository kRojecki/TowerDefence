from Game.Core.GameArea import GameArea
from Game.Core.Screen.AbstractScreen import AbstractScreen


class GameScreen(AbstractScreen):

    gameArea = 0

    def __init__(self, configuration):
        super().__init__(configuration)
        self.gameArea = GameArea(configuration)

    def init(self):
        self.gameArea.init()

    def update(self, screen):
        self.gameArea.update(screen)

