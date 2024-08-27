# import json

# class ConfigManager:
#     def __init__(self, config_path='config.json'):
#         self.config_path = config_path
#         self.load_config()

#     def load_config(self):
#         with open(self.config_path, 'r') as file:
#             self.config = json.load(file)

#     def get_config(self):
#         return self.config

import json
import os
from dotenv import load_dotenv

class ConfigManager:
    def __init__(self, config_path='config.json'):
        load_dotenv()  # Load environment variables from .env file
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as file:
            self.config = json.load(file)
        
        # Override or add environment variables from the .env file to the config
        self.config['aws_access_key'] = os.getenv('AWS_ACCESS_KEY')
        self.config['aws_secret_key'] = os.getenv('AWS_SECRET_KEY')

    def get_config(self):
        return self.config
