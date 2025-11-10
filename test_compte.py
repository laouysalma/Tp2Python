from compte_bancaire import MonCompte

compte_salma = MonCompte("Salma", 1500)
compte_salma.ajouter_argent(350)
compte_salma.retirer_argent(20)
print(compte_salma)
print("Solde actuel :", compte_salma.solde)

try:
    compte_salma.solde = 1000
except AttributeError as e:
    print("Erreur :", e)

compte_salma.voir_historique()
