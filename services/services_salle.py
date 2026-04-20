# services/service_salle.py

from data.dao_salle import DataSalle
from models.salle import Salle

class ServiceSalle:

    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle: Salle):
        # Vérifier que toutes les données sont présentes
        if not salle.code or not salle.description or not salle.categorie or salle.capacite is None:
            return False, "Toutes les informations doivent être fournies."

        # Vérifier capacité >= 1
        if salle.capacite < 1:
            return False, "La capacité doit être >= 1."

        # Appeler le DAO
        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutée avec succès."

    def modifier_salle(self, salle: Salle):
        # Vérifier que toutes les données sont présentes
        if not salle.code or not salle.description or not salle.categorie or salle.capacite is None:
            return False, "Toutes les informations doivent être fournies."

        # Vérifier capacité >= 1
        if salle.capacite < 1:
            return False, "La capacité doit être >= 1."

        # Appeler le DAO
        self.dao_salle.update_salle(salle)
        return True, "Salle modifiée avec succès."

    def supprimer_salle(self, code: str):
        self.dao_salle.delete_salle(code)
        return True, "Salle supprimée."

    def rechercher_salle(self, code: str):
        return self.dao_salle.get_salle(code)

    def recuperer_salles(self):
        return self.dao_salle.get_salles()
