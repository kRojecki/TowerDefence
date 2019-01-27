from Configuration.General.ConfigurationParser import ConfigurationParser


class Configuration:

    _configuration = None

    @staticmethod
    def init():
        Configuration._configuration = ConfigurationParser.load_configuration()

    @staticmethod
    def get_int(section, key):
        return int(Configuration._get_configuration_value(section,key));

    @staticmethod
    def get_str(section, key):
        return Configuration._get_configuration_value(section, key);

    @staticmethod
    def _get_configuration_value(section, key):
        try:
            return Configuration._configuration[section][key]
        except Exception:
            raise Exception('Config key ['+section+']['+key+'] not found!')
