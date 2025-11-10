from mon_client import Client, CompteBancaire

cli = Client("Fouad")
compte1 = CompteBancaire()
compte2 = CompteBancaire(500)

cli.ajouter_compte(compte1)
cli.ajouter_compte(compte2)

compte1.deposer(300)
compte1.retirer(50)
compte2.retirer(100)

cli.afficher()

compte1.relevé_operations()
compte2.relevé_operations()
