import json

class ConfigLoader:
    @staticmethod
    def load(path):
        with open(path) as f:
            return json.load(f)
