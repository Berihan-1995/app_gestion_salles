import json

class DaoSalle:
    def __init__(self, config_path="data/config.json"):
        self.config_path = config_path

    def charger_salles(self):
        try:
            with open(self.config_path, "r") as f:
                data = json.load(f)
                return data.get("salles", [])
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def sauvegarder_salles(self, salles):
        with open(self.config_path, "w") as f:
            json.dump({"salles": salles}, f, indent=4)
