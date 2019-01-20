import random

from Game.Objects.Tile.Path.EnemyPath import EnemyPath
from Game.Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Objects.Enemy.Enum.EnemyEnum import EnemyEnum
from Utils.Constant import Position
from Utils.Constant.EventEnum import EventEnum
from Utils.Constant.SubEventEnum import SubEventEnum


class EnemyStartingPointPath(EnemyPath):

    _new_wave = True

    def update(self, nearest_enemy_position=None):
            if self._new_wave:
                EventDispatcher.dispatch(
                    EventEnum.ENEMY,
                    SubEventEnum.NEW_ENEMY_WAVE,
                    {
                        "start_position_range": (
                            [
                                (self.get_position()[Position.X] - self.get_size()[Position.X])*4,
                                self.get_position()[Position.X],
                            ],
                            [
                                self.get_position()[Position.Y] + int(self.get_size()[Position.Y]/2) - 5,
                                self.get_position()[Position.Y] + int(self.get_size()[Position.Y]/2) + 5
                            ]
                        ),
                        "enemy_types": [
                            EnemyEnum.ROUND_ENEMY,
                            EnemyEnum.TRIANGLE_ENEMY,
                            EnemyEnum.SQUARE_ENEMY,
                            EnemyEnum.ROUND_ENEMY,
                            EnemyEnum.SQUARE_ENEMY,
                            EnemyEnum.TRIANGLE_ENEMY,
                            EnemyEnum.SQUARE_ENEMY,
                            EnemyEnum.ROUND_ENEMY,
                        ],
                    }
                )
                self._new_wave = False
