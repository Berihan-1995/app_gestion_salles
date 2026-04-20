# Service permettant de gérer les salles


from data.dao_salle import DaoSalle
from models.salle import Salle

class ServiceSalle:
    def __init__(self):
        self.dao = DaoSalle()

    def get_all_salles(self):
        data = self.dao.charger_salles()
        salles = []
        for s in data:
            salle = Salle(s["id_salle"], s["nom"], s["capacite"])
            salles.append(salle)
        return salles

    def ajouter_salle(self, id_salle, nom, capacite):
        salles = self.dao.charger_salles()

        for s in salles:
            if s["id_salle"] == id_salle:
                raise ValueError("ID déjà utilisé")

        if capacite <= 0:
            raise ValueError("Capacité invalide")

        nouvelle_salle = {
            "id_salle": id_salle,
            "nom": nom,
            "capacite": capacite
        }

        salles.append(nouvelle_salle)
        self.dao.sauvegarder_salles(salles)

    def supprimer_salle(self, id_salle):
        salles = self.dao.charger_salles()
        nouvelles_salles = []

        for s in salles:
            if s["id_salle"] != id_salle:
                nouvelles_salles.append(s)

        self.dao.sauvegarder_salles(nouvelles_salles)
