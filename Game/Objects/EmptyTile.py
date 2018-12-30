import pygame
from Game.Objects.Tile import Tile

class EmptyTile(Tile):

    def __init__(self, position):
        self.position = position
