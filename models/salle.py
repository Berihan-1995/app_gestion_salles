
class Salle:
    def __init__(self, code: str, description: str, categorie: str, capacite: int):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite


    def afficher_infos(self):
        print(f"Code : {self.code}")
        print(f"Description : {self.description}")
        print(f"Catégorie : {self.categorie}")
        print(f"Capacité : {self.capacite}")

    def __str__(self):
        return f"Salle({self.code}, {self.description}, {self.categorie}, {self.capacite})"
