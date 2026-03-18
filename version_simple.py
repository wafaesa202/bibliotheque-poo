# version_simple.py
livres = []

def ajouter_livre():
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    livre = {"titre": titre, "auteur": auteur}
    livres.append(livre)
    print("Livre ajouté avec succès !")

def afficher_livres():
    if not livres:
        print("Aucun livre")
        return
    for i, livre in enumerate(livres, 1):
        print(f"{i}. {livre['titre']} - {livre['auteur']}")

def rechercher_livre():
    titre = input("Titre à rechercher : ")
    trouve = [l for l in livres if l['titre'].lower() == titre.lower()]
    if trouve:
        for l in trouve:
            print(f"{l['titre']} - {l['auteur']}")
    else:
        print("Livre non trouvé")

def supprimer_livre():
    titre = input("Titre à supprimer : ")
    for l in livres:
        if l['titre'].lower() == titre.lower():
            livres.remove(l)
            print("Livre supprimé")
            return
    print("Livre non trouvé")

def menu():
    while True:
        print("\n===== MENU BIBLIOTHEQUE =====")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Rechercher un livre")
        print("4. Supprimer un livre")
        print("5. Quitter")

        choix = input("Votre choix : ")
        if choix == "1":
            ajouter_livre()
        elif choix == "2":
            afficher_livres()
        elif choix == "3":
            rechercher_livre()
        elif choix == "4":
            supprimer_livre()
        elif choix == "5":
            break
        else:
            print("Choix invalide")

menu()