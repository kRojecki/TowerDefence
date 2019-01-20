import configparser


class ConfigurationParser:

    @staticmethod
    def load_configuration(filename='config.ini'):
        config = configparser.ConfigParser()
        config.read(filename)

        return config

