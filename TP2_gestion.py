class Account:
    def __init__(self, solde_initial = 0):
        self.solde_initial = solde_initial
        self.solde_actuel = solde_initial

    def getBalance(self):
        return self.solde_actuel
    def compte_depot(self, montant_deposer):
        self.solde_actuel = self.solde_actuel+montant_deposer

    def compte_retrait(self, montant_retirer):
        self.solde_actuel = self.solde_actuel-montant_retirer
    def compte_interet(self,taux_interet):
        self.solde_actuel = self.solde_actuel * (1+taux_interet)

affiche = Account()
affiche.compte_depot(100)
affiche.compte_retrait(20)
affiche.compte_interet(2)
print(affiche.getBalance())