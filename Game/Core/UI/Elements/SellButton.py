from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Core.UI.Elements.Abstract.Button import Button
from Utils.Constant import Color, PointableState
from Utils.Constant.Event.EventEnum import EventEnum
from Utils.Constant.Event.SubEventEnum import SubEventEnum


class SellButton(Button):

    _size = (25, 25)

    _background_color = {
        PointableState.CLEAR: Color.DARKER_RED,
        PointableState.HOVER: Color.DARK_RED,
        PointableState.CLICKED: Color.LIGHT_GRAY,
    }

    def _click_action(self, pressed):
        EventDispatcher.dispatch(
            EventEnum.LEVEL,
            SubEventEnum.TURRET_SOLD,
            {
                'tile': self._linked_element
            }
        )

