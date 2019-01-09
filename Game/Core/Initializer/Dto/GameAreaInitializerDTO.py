class GameAreaInitializerDTO:

    field_size = 0
    file_path = ''

    def __init__(self, field_size, file_path=''):
        self.field_size = field_size
        self.file_path = file_path
