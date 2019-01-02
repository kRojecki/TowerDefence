import configparser


class ConfigurationParser:

    @staticmethod
    def load_configuration():
        config = configparser.ConfigParser();
        config.read('config.ini')

        return config

