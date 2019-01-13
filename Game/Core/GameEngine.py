import sys
import pygame
from Game.Utils.Constant import Color
from Game.Core.Screen.GameScreen import GameScreen
from Game.Configuration.ConfigurationParser import ConfigurationParser
from Game.Core.Event.Handler.EventHandler import EventHandler


class GameEngine:

    FIXED_FPS = 60

    _width, _height = 1024, 768
    _clock = 0
    _main_surface = 0
    _current_screen = 0

    config = None
    _event_handler = None

    def init(self):
        self.config = ConfigurationParser.load_configuration()
        self._event_handler = EventHandler()
        pygame.init()

    def setup(self):
        size = (self.config.getint('DISPLAY', 'resolution.width'), self.config.getint('DISPLAY', 'resolution.height'))
        pygame.display.set_mode(size)

        pygame.display.set_caption(self.config.get('DISPLAY', 'window.title'))

        self._main_surface = pygame.display.set_mode(size)
        self._clock = pygame.time.Clock()

        self._current_screen = GameScreen(self.config)
        self._current_screen.init()

    def run(self):
        self.loop()

    def loop(self):
        while True:
            # set clock to fixed 60 fps
            self._clock.tick(self.FIXED_FPS)

            # handle system events like closing aplication
            self.handle_events()

            # fill whole area in color, everything is redrawed every frame
            self._main_surface.fill(Color.BLACK)

            # update screen by actual screen
            self._current_screen.update(self._main_surface)

            # flip buffers to show prepared frame
            pygame.display.flip()

    def handle_events(self):
        self._event_handler.handle()

    @staticmethod
    def exit(self):
        print(self.config.get('GAME', 'quit.message'))
        sys.exit()
