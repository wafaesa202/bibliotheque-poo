class Livre:
    def __init__(self, id, titre, auteur):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print("Livre emprunté")
        else:
            print("Livre non disponible")

    def retourner(self):
        self.disponible = True
        print("Livre retourné")