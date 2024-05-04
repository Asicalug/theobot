import json
import os

class Settings:
    def __init__(self):
        if not os.path.exists("./settings.json"):
            with open("./settings.json", "w") as f:
                f.write("{}")
        self.settings = json.load(open("./settings.json", "r"))

    def get(self, key: str):
        keys = key.split('.')
        obj = self.settings
        for k in keys:
            obj = obj.get(k, None)
            if obj is None:
                break
        return obj

    def set(self, key: str, value):
        keys = key.split('.')
        obj = self.settings
        for k in keys[:-1]:
            if k not in obj:
                obj[k] = {}
            obj = obj[k]
        obj[keys[-1]] = value
        self._save_settings()

    def remove(self, key: str):
        keys = key.split('.')
        obj = self.settings
        for k in keys[:-1]:
            if k not in obj:
                return  # The key does not exist, nothing to remove
            obj = obj[k]
        if keys[-1] in obj:
            del obj[keys[-1]]  # Remove the specified key
        self._save_settings()

    def _save_settings(self):
        with open("./settings.json", "w") as f:
            json.dump(self.settings, f, indent=4)