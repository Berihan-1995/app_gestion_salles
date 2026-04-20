# cette classe Salle représente une salle avec son nom et sa capacité

class Salle:
    def __init__(self, id_salle: int, nom: str, capacite: int):
        self.id_salle = id_salle
        self.nom = nom
        self.capacite = capacite

    def __str__(self):
        return f"Salle(id={self.id_salle}, nom='{self.nom}', capacite={self.capacite})"

    def __str__(self):
        return f"Salle {self.id_salle} - {self.nom} ({self.capacite} places)"

