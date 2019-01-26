from Core.Event.Dispatcher.EventDispatcher import EventDispatcher
from Game.Core.Factory.EnemyFactory import EnemyFactory
from Utils.Constant.Event.EventEnum import EventEnum
from Utils.Constant.Event.SubEventEnum import SubEventEnum


class EnemyEventHandler:

    _enemyCollection = None

    _path = None

    @staticmethod
    def register_object(collection):
        EnemyEventHandler._enemyCollection = collection

    @staticmethod
    def set_enemy_path(path):
        EnemyEventHandler._path = path

    @staticmethod
    def handle(event):
        method_name = getattr(EnemyEventHandler, event.sub_event)
        method_name(event)

    @staticmethod
    def _enemy_killed(event):
        try:
            EnemyEventHandler._enemyCollection.remove(event.enemy)
            EventDispatcher.dispatch(
                EventEnum.UI,
                SubEventEnum.ADD_SCORE,
                {
                    "score": event.enemy.get_score(),
                }
            )
            EventDispatcher.dispatch(
                EventEnum.UI,
                SubEventEnum.ADD_FUNDS,
                {
                    "money": event.enemy.get_money(),
                }
            )
        except ValueError:
            pass

    @staticmethod
    def _new_enemy_wave(event):
        enemies = EnemyFactory.create_enemy_from_event(event, EnemyEventHandler._path)
        for enemy in enemies:
            EnemyEventHandler._enemyCollection.append(enemy)

    @staticmethod
    def _enemy_completed_path(event):
        pass

    @staticmethod
    def _enemy_remove(event):
        EnemyEventHandler._enemyCollection.remove(event.enemy)
