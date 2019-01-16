from Core.Path.Path import Path
from Core.Path.PathStep import PathStep
from Game.Objects.Tile.Path.EnemyStartingPointPath import EnemyStartingPointPath
from Game.Objects.Tile.Path.EnemyEndPointPath import EnemyEndPointPath
from Game.Objects.Tile.Path.EnemyPath import EnemyPath
from Utils.Constant import Position
from Utils.Helper.DataSetHelper.TupleTransformer import TupleTransformer


class PathResolver:

    _NEIGHBORHOOD_POSITIONS = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    ]

    _game_area = None

    _start_point = None
    _end_point = None

    _path = []
    _visited_tiles = []

    def generate_path(self, game_area):

        self._game_area = game_area
        self._get_border_points()

        self._build_path(self._start_point)

        return Path(self._path)

    def _get_border_points(self):
        for row in self._game_area:
            for field in row:
                if isinstance(field, EnemyStartingPointPath):
                    self._start_point = field
                    continue

                if isinstance(field, EnemyEndPointPath):
                    self._end_point = field
                    continue

    def _get_neighbor_tiles(self, tile_position):
        neighborhood = []

        for position in self._NEIGHBORHOOD_POSITIONS:

            neighborhood_position = TupleTransformer.add_tuples(tile_position, position)

            if neighborhood_position[Position.X] < 0 \
                    or neighborhood_position[Position.Y] < 0 \
                    or neighborhood_position[Position.X] > len(self._game_area[0]) \
                    or neighborhood_position[Position.Y] > len(self._game_area):
                continue

            neighborhood.append(
                self._game_area[neighborhood_position[Position.Y]][neighborhood_position[Position.X]]
            )

        return neighborhood

    def _build_path(self, tile):

        if isinstance(tile, EnemyEndPointPath):
            return False

        neighbors = self._get_neighbor_tiles(tile.get_tile_position())

        for neighbor in neighbors:
            if neighbor not in self._visited_tiles \
                    and isinstance(neighbor, EnemyPath) and not isinstance(neighbor, EnemyStartingPointPath):
                    self._create_path_step(neighbor)
                    self._visited_tiles.append(tile)
                    self._build_path(neighbor)

    def _create_path_step(self, tile):

        length = 40

        if isinstance(tile, EnemyEndPointPath):
            length *= 2

        if len(self._path) == 0:
            self._path.append(
                PathStep(
                    length,
                    self._get_move_vector(self._start_point.get_tile_position(), tile.get_tile_position()),
                    self._start_point.get_tile_position()
                )
            )

        self._path.append(
            PathStep(
                length,
                self._get_move_vector(self._path[-1].get_tile_position(), tile.get_tile_position()),
                tile.get_tile_position()
            )
        )

    def _get_move_vector(self, previous, forward):
        return (
            forward[Position.X] - previous[Position.X],
            forward[Position.Y] - previous[Position.Y]
        )
