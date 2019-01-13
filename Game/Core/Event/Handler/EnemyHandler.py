from Game.Utils.Constant import EventEnum
from Game.Core.Factory.EnemyFactory import EnemyFactory


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
        if event.type == EventEnum.ENEMY_KILLED:
            EnemyHandler._enemy_killed(event)

        if event.type == EventEnum.NEW_ENEMY_WAVE:
            EnemyHandler._new_enemy_wave(event)

        if event.type == EventEnum.ENEMY_COMPLETED_PATH:
            EnemyHandler._enemy_completed_path(event)

    @staticmethod
    def _enemy_killed(event):
        try:
            EnemyHandler._enemyCollection.remove(event.enemy)
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
