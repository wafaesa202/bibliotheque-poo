class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                self.livres.remove(livre)
                print("Livre supprimé")
                return
        print("Livre non trouvé")

    def rechercher_livre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                return livre
        return None

    def afficher_livres(self):
        if not self.livres:
            print("Aucun livre")
            return
        for livre in self.livres:
            dispo = "Disponible" if livre.disponible else "Emprunté"
            print(f"{livre.id} - {livre.titre} - {livre.auteur} - {dispo}")