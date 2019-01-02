import sys
import pygame
from Utils.Constant import Color
from Game.Core.Screen.GameScreen import GameScreen


class GameEngine:

    width, height = 1024, 768
    clock = 0
    main_surface = 0
    current_screen = 0

    def init(self):
        pygame.init()

        size = (self.width, self.height)
        pygame.display.set_mode(size)

        self.main_surface = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        self.current_screen = GameScreen()
        self.current_screen.init_screen()

    def run(self):

        self.loop()

    def loop(self):
        while True:
            # set clock to fixed 60 fps
            self.clock.tick(60)

            # handle system events like closing aplication
            self.handleSystemEvents()

            # fill whole area in color, everything is redrawed every frame
            self.main_surface.fill(Color.BLACK)

            # update screen by actual screen
            self.current_screen.update(self.main_surface)

            # flip buffers to show prepared frame
            pygame.display.flip()

    def handleSystemEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

    def exit(self):
        print('I\'ll be back!')
        sys.exit()
