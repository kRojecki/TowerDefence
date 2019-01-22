from Core.Event.Handler.UIHandler import UIHandler
from Core.UI.UserInterface import UserInterface
from Game.Core.Level import Level
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

        UIHandler.register_object(self._user_interface)

    def update(self, screen):
        self._level.update()
        self._level.draw(screen)
        self._user_interface.draw(screen)

