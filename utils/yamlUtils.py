import yaml

from utils.logging_use import Logger
from config.config import YAML_LOG,API_YAML,BASE_DIR


class YamlUtils:

    logger = Logger.init_log_config(__name__, YAML_LOG)

    @staticmethod
    def _handle_error(e, operation, path=None):
        if isinstance(e, FileNotFoundError):
            YamlUtils.logger.error(f"in{operation}process，File not found: {path}")
            return None
        if isinstance(e, yaml.YAMLError):
            YamlUtils.logger.error(f"in{operation}process，Error parsing YAML file: {e}")
            return None
        if isinstance(e, KeyError):
            YamlUtils.logger.error(f"in{operation}process,invalid key")
            return None
        else:
            YamlUtils.logger.error(f"in{operation}process,An unexpected error occurred: {e}")
            return None

    @staticmethod
    def read_data(path, key=None, user=''):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.load(stream=f, Loader=yaml.FullLoader)
                if key:
                    YamlUtils.logger.info(f"path：{path}，read data success,\n  operator is ：{user}")
                    return data[key]
                else:
                    YamlUtils.logger.info(f"path：{path}，read data success,\n  operator is ：{user}")
                    return data
        except Exception as e:
            YamlUtils._handle_error(e, "reading", path)
            return None

if __name__ == '__main__':
    yaml_utils = YamlUtils()
    api_url = yaml_utils.read_data(API_YAML)
    print(api_url)
