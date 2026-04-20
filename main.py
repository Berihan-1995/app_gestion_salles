# ce Programme affiche le menu de gestion des salles

from views.view_salle import ViewSalle

def main():
    vue = ViewSalle()
    choix = ""

    while choix != "5":
        vue.afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            vue.afficher_salles()
        elif choix == "2":
            vue.ajouter_salle()
        elif choix == "3":
            vue.supprimer_salle()
        elif choix == "4":
            vue.rechercher_salle()
        elif choix == "5":
            print("Au revoir.")
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()

