import json
from dotenv import load_dotenv
import os

class ConfigManager:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as file:
            self.config = json.load(file)

        self.config['aws_access_key'] = os.getenv('AWS_ACCESS_KEY')
        self.config['aws_secret_key'] = os.getenv('AWS_SECRET_KEY')


    def get_config(self):
        return self.config

