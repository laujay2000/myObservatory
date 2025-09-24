import yaml
import os


# 读取YAML配置文件
class Config:

    def __init__(self, config_file="config.yaml"):
        config_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            config_file
        )

        self.config = self.load_config(config_path)

    # 加载YAML配置文件
    @staticmethod
    def load_config(config_file: str) -> dict:
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r', encoding='utf-8') as f:
                    return yaml.safe_load(f) or {}
            return {}
        except Exception as e:
            print(f"加载配置失败: {e}")
            return {}

    # 获取配置值
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value
