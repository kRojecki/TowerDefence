from Game.Core.GameArea import GameArea
from Game.Core.Screen.AbstractScreen import AbstractScreen


class GameScreen(AbstractScreen):

    gameArena = 0

    def __init__(self):
        self.gameArea = GameArea()
        pass

    def init_screen(self):
        self.gameArea.init_field()

    def update(self, screen):
        screen.blit(self.gameArea.update(), (10, 10))

