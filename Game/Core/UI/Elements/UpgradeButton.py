from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Core.UI.Elements.Abstract.Button import Button
from Utils.Constant import Color, PointableState
from Utils.Constant.Event.EventEnum import EventEnum
from Utils.Constant.Event.SubEventEnum import SubEventEnum


class UpgradeButton(Button):

    _size = (25, 25)

    _background_color = {
        PointableState.CLEAR: Color.DARKER_GREEN,
        PointableState.HOVER: Color.DARK_GREEN,
        PointableState.CLICKED: Color.GREEN,
        }

    def _click_action(self, pressed):
        EventDispatcher.dispatch(
            EventEnum.TILE,
            SubEventEnum.TURRET_UPGRADE,
            {
                'tile': self._linked_element
            }
        )
