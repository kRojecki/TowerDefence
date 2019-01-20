import pygame

from Configuration.Configuration import Configuration
from Core.Screen.ScreenResolver import ScreenResolver
from Game.Utils.Constant import Color
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
        Configuration.init()
        pygame.init()
        self._event_handler = EventHandler()

    def setup(self):
        size = (
            Configuration.get_int('DISPLAY', 'resolution.width'),
            Configuration.get_int('DISPLAY', 'resolution.height')
        )
        pygame.display.set_mode(size)

        pygame.display.set_caption(Configuration.get_str('DISPLAY', 'window.title'))

        self._main_surface = pygame.display.set_mode(size)
        self._clock = pygame.time.Clock()

        self._current_screen = ScreenResolver.create_screen(Configuration.get_str('GAME', 'screen.start'), self.config)
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
