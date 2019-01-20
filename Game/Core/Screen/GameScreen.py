from Game.Core.Level import Level
from Game.Core.Screen.AbstractScreen import AbstractScreen


class GameScreen(AbstractScreen):

    game_area = 0

    def __init__(self, configuration):
        super().__init__(configuration)
        self.game_area = Level(configuration)

    def init(self):
        self.game_area.init()

    def update(self, screen):
        self.game_area.update()
        self.game_area.draw(screen)

