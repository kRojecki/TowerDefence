import pygame

from Configuration.Configuration import Configuration
from Core.Screen.ScreenResolver import ScreenResolver
from Game.Utils.Constant import Color
from Game.Core.Event.Handler.EventHandler import EventHandler
from Utils.Constant.EventEnum import EventEnum


class GameEngine:

    FIXED_FPS = 60

    _width, _height = 1024, 768
    _clock = None
    _main_surface = None
    _current_screen = None

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

        self._font_setup()

        pygame.event.set_allowed(
            EventEnum.get_allowed_events()
        )

    def run(self):
        self.loop()

    def loop(self):
        while True:
            # set clock to fixed 60 fps
            self._clock.tick(self.FIXED_FPS)

            # handle system events like closing aplication
            self._handle_events()

            # fill whole area in color, everything is redrawed every frame
            self._main_surface.fill(Color.BLACK)

            # update screen by actual screen
            self._current_screen.update(self._main_surface)

            # flip buffers to show prepared frame
            pygame.display.flip()

    def _handle_events(self):
        self._event_handler.handle()

    def _font_setup(self):
        self.font = pygame.font.SysFont("monospace", 10)
