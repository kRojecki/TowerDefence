class FileMapLoader:
    def load_level(self, path):
        file = open(path, 'r')
        return self._sanitize(file.readlines())

    def _sanitize(self, lines):

        lines[:] = [s.rstrip() for s in lines]

        return lines
