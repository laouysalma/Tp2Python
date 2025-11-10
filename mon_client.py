from datetime import datetime

class CompteBancaire:
    _id_compte = 1

    def __init__(self, solde_initial=0.0):
        self.__solde = solde_initial
        self.id = CompteBancaire._id_compte
        CompteBancaire._id_compte += 1
        self._historique = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._historique.append(f"{datetime.now()}: Déposé {montant} €")
        else:
            print("Montant invalide pour le dépôt.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._historique.append(f"{datetime.now()}: Retiré {montant} €")
        else:
            print("Fonds insuffisants ou montant invalide.")

    def get_solde(self):
        return self.__solde

    def relevé_operations(self):
        print(f"Relevé des opérations pour le compte {self.id}:")
        for op in self._historique:
            print("-", op)


class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []

    def ajouter_compte(self, compte):
        self.comptes.append(compte)

    def afficher(self):
        print(f"Client : {self.nom}")
        for compte in self.comptes:
            print(f"  Compte {compte.id} - Solde : {compte.get_solde()} €")
