from Utils.Helper.ClassProvider import ClassProvider


class ScreenResolver:

    MENU_SCREEN = 'Game.Core.Screen.MenuScreen.MenuScreen'
    GAME_SCREEN = 'Game.Core.Screen.GameScreen.GameScreen'

    ON_START_SCREEN = MENU_SCREEN

    @staticmethod
    def create_screen(screen_name):
        return ClassProvider.provide_class(screen_name)()
