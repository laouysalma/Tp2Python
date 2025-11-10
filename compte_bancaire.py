class MonCompte:
    def __init__(self, nom_proprietaire, solde_depart=0):
        self._nom = nom_proprietaire
        self.__argent = solde_depart
        self._historique = []

    def ajouter_argent(self, montant):
        if montant > 0:
            self.__argent += montant
            self._historique.append(f"Ajouté : {montant} €")
        else:
            print("Erreur : montant invalide.")

    def retirer_argent(self, montant):
        if 0 < montant <= self.__argent:
            self.__argent -= montant
            self._historique.append(f"Retiré : {montant} € ")
        else:
            print("Erreur : fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        return self.__argent

    def voir_historique(self):
        print(f"Historique des opérations pour {self._nom} :")
        for action in self._historique:
            print("-", action)

    def __str__(self):
        return f"Propriétaire : {self._nom}, Solde : {self.solde} € "
