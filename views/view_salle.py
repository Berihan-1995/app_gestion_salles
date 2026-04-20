from services.services_salle import ServiceSalle

class ViewSalle:
    def __init__(self):
        self.service = ServiceSalle()

    def afficher_menu(self):
        print("1. Afficher les salles")
        print("2. Ajouter une salle")
        print("3. Supprimer une salle")
        print("4. Quitter")

    def afficher_salles(self):
        salles = self.service.get_all_salles()
        for s in salles:
            print(s)

    def ajouter_salle(self):
        id_salle = int(input("ID de la salle : "))
        nom = input("Nom de la salle : ")
        capacite = int(input("Capacité : "))
        self.service.ajouter_salle(id_salle, nom, capacite)
        print("Salle ajoutée.")

    def supprimer_salle(self):
        id_salle = int(input("ID de la salle à supprimer : "))
        self.service.supprimer_salle(id_salle)
        print("Salle supprimée.")
