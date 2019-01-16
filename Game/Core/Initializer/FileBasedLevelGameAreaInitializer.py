from Game.Core.Initializer.GameAreaInitializer import GameAreaInitializer
from Game.Core.Loader.FileMapLoader import FileMapLoader
from Game.Core.Parser.FileMapParser import FileMapParser
from Game.Core.Path.PathResolver import PathResolver


class FileBasedLevelGameAreaInitializer(GameAreaInitializer):

    _file_loader = None
    _path_resolver = None


    def __init__(self):
        self._file_loader = FileMapLoader()
        self._path_resolver = PathResolver()


    def init_game_area(self, dto):

        map_parser = FileMapParser(dto.field_size)

        file_lines = self._file_loader.load_level(dto.file_path)
        game_area = map_parser.parse(file_lines)

        path = self._path_resolver.generate_path(game_area)

        return [game_area, path]
