# config_manager.py
import os
import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG_PATH = os.path.join(SCRIPT_DIR, 'config', 'default_config.yaml')

class ConfigurationManager:
    def __init__(self, config_path='config.yaml'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        config_path = os.path.join(SCRIPT_DIR, self.config_path)
        config_data = self.load_default_config()

        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data.update(yaml.safe_load(f) or {})

        return config_data

    def load_default_config(self):
        with open(DEFAULT_CONFIG_PATH, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}

    def get_config(self):
        return self.config
