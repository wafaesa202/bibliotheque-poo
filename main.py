from models.bibliotheque import Bibliotheque
from models.livre import Livre

def menu():
    biblio = Bibliotheque()

    while True:
        print("\n===== MENU BIBLIOTHEQUE POO =====")
        print("1. Ajouter un livre")
        print("2. Afficher les livres")
        print("3. Rechercher un livre")
        print("4. Supprimer un livre")
        print("5. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            livre = Livre(len(biblio.livres)+1, titre, auteur)
            biblio.ajouter_livre(livre)

        elif choix == "2":
            biblio.afficher_livres()

        elif choix == "3":
            titre = input("Titre : ")
            livre = biblio.rechercher_livre(titre)
            if livre:
                print(f"{livre.id} - {livre.titre} - {livre.auteur}")
            else:
                print("Livre non trouvé")

        elif choix == "4":
            titre = input("Titre : ")
            biblio.supprimer_livre(titre)

        elif choix == "5":
            break

        else:
            print("Choix invalide")

menu()