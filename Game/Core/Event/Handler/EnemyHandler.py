from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Game.Core.Factory.EnemyFactory import EnemyFactory
from Utils.Constant.EventEnum import EventEnum
from Utils.Constant.SubEventEnum import SubEventEnum


class EnemyHandler:

    _enemyCollection = None

    _path = None

    @staticmethod
    def register_object(collection):
        EnemyHandler._enemyCollection = collection

    @staticmethod
    def set_enemy_path(path):
        EnemyHandler._path = path

    @staticmethod
    def handle(event):
        method_name = getattr(EnemyHandler, event.sub_event)
        method_name(event)

    @staticmethod
    def _enemy_killed(event):
        try:
            EnemyHandler._enemyCollection.remove(event.enemy)
            EventDispatcher.dispatch(
                EventEnum.LEVEL,
                {
                    "sub_event": SubEventEnum.ADD_SCORE,
                    "score": event.enemy.get_score(),
                }
            )
        except ValueError:
            pass

    @staticmethod
    def _new_enemy_wave(event):
        enemies = EnemyFactory.create_enemy_from_event(event, EnemyHandler._path)
        for enemy in enemies:
            EnemyHandler._enemyCollection.append(enemy)

    @staticmethod
    def _enemy_completed_path(event):
        pass

    @staticmethod
    def _enemy_remove(event):
        EnemyHandler._enemyCollection.remove(event.enemy)
