import pygame


class GameEngine:

    width, height = 1024, 768
    size = width, height

    def __init__(self):
        pass

    def init(self):
        pygame.init()
        pygame.display.set_mode(self.size)



