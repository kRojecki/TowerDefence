from Game.Utils.Constant import EventEnum

class EnemyHandler:

    _enemyCollection = None

    @staticmethod
    def register_object(collection):
        EnemyHandler._enemyCollection = collection

    @staticmethod
    def handle(event):
        if event.type == EventEnum.ENEMY_KILLED:
            try:
                EnemyHandler._enemyCollection.remove(event.enemy)
            except ValueError:
                pass

