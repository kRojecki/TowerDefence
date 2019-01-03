import sys
import pygame
from Utils.Constant import Color
from Game.Core.Screen.GameScreen import GameScreen
from Game.Configuration.ConfigurationParser import ConfigurationParser
from Game.Core.Handler.EventHandler import EventHandler


class GameEngine:

    width, height = 1024, 768
    clock = 0
    main_surface = 0
    current_screen = 0

    config = 0

    input_controller = 0

    def init(self):
        self.config = ConfigurationParser.load_configuration()
        self.input_controller = EventHandler()
        pygame.init()

    def setup(self):
        size = (self.config.getint('DISPLAY', 'resolution.width'), self.config.getint('DISPLAY', 'resolution.height'))
        pygame.display.set_mode(size)

        pygame.display.set_caption(self.config.get('DISPLAY', 'window.title'))

        self.main_surface = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        self.current_screen = GameScreen(self.config)
        self.current_screen.init()

    def run(self):
        self.loop()

    def loop(self):
        while True:
            # set clock to fixed 60 fps
            self.clock.tick(60)

            # handle system events like closing aplication
            self.handle_system_events()

            # fill whole area in color, everything is redrawed every frame
            self.main_surface.fill(Color.BLACK)

            # update screen by actual screen
            self.current_screen.update(self.main_surface)

            # flip buffers to show prepared frame
            pygame.display.flip()

    def handle_system_events(self):
        self.input_controller.handle()

    @staticmethod
    def exit(self):
        print(self.config.get('GAME', 'quit.message'))
        sys.exit()
