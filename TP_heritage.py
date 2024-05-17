class Utilisateurs:
    def __int__(self, nom, mot_de_passe):
        self.nom = nom
        self.mot_de_passede = mot_de_passe
    def inscrire(self,nom, mot_de_passe):
        self.nom = nom
        self.mot_de_passede = mot_de_passe
    def connecter(self):
        pass
    def cree_fils_disc(self):
        pass
    def repondre_message(self):
        pass
    def cree_post(self):
        pass
class Moderateurs(Utilisateurs):
    def modifier_post(self):
        pass
    def supprimer_post(self):
        pass

class Fils_discussion:
    def __init__(self, titre, date_creation, collection):
        self.titre = titre
        self.date_creation = date_creation
        self.collection = collection
        self.posts = []
class Fichier:
    def __init__(self, name, taille, extension):
        self.name = name
        self.taille = taille
        self.extension = extension

class Posts(Fils_discussion,Fichier):
    def __init__(self, texte, utilisateur, date_publication, fichier_attache):
        self.texte = texte
        self.utilisateur = utilisateur
        self.date_publication = date_publication
        self.fichier_attache = fichier_attache
    def afficher_post(self):
        print(f" Titre {self.titre} avec texte {self.texte} taille de {self.taille} avec un extension{self.date_publication}")