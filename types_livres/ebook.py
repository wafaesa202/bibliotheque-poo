from models.livre import Livre

class Ebook(Livre):
    def __init__(self, id, titre, auteur, taille):
        super().__init__(id, titre, auteur)
        self.taille = taille