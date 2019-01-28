class AbstractFileLoader:

    def load(self, path):
        file = open(path, 'r')
        return self._sanitize(file.readlines())

    @staticmethod
    def _sanitize(lines):
        lines[:] = [s.rstrip() for s in lines]

        return lines
