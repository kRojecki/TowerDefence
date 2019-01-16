import random

from Game.Utils.Helper.ClassProvider import ClassProvider


class EnemyFactory:

    DEFAULT_ENEMY = 'Game.Objects.Enemy.RoundEnemy.RoundEnemy'

    @staticmethod
    def create_enemy_from_event(event, path):
        return EnemyFactory.create_enemy_from_args(event.start_position_range, event.enemy_types, path)

    @staticmethod
    def create_enemy_from_args(position_range, enemy_types, path):
        enemies = []
        for enemy_type in enemy_types:
            position = (
                position_range[0][0] if position_range[0][0] == position_range[0][1] else random.randrange(position_range[0][0], position_range[0][1]),
                position_range[1][0] if position_range[1][0] == position_range[1][1] else random.randrange(position_range[1][0], position_range[1][1]),
            )

            enemies.append(ClassProvider.provide_class(enemy_type)(position, path))
        return enemies


