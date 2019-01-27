from Core.Event.Handler.UIEventHandler import UIEventHandler
from Core.UI.UserInterface import UserInterface
from Core.Level.Level import Level
from Game.Core.Screen.AbstractScreen import AbstractScreen


class GameScreen(AbstractScreen):

    _level = None
    _user_interface = None

    def __init__(self):
        self._level = Level()
        self._user_interface = UserInterface()

    def init(self):
        self._level.init()
        self._user_interface.init()

        UIEventHandler.register_object(self._user_interface)

    def update(self, screen):
        self._level.update()
        self._level.draw(screen)
        self._user_interface.draw(screen)

