# Visibilité des attributs et méthodes

class CompteBancaire:
    def __init__(self, proprietaire, solde=0):
        self.proprietaire = proprietaire  # Attribut public
        self.solde = solde  # Attribut public
        self._numero_compte = "123456"  # Attribut protégé
        self.__pin = "0000"  # Attribut privé

    def deposer(self, montant):
        self.solde += montant
        print(f"Dépôt de {montant}. Nouveau solde: {self.solde}")
    
    def retirer(self, montant, pin):
        if pin == self.__pin:
            if montant <= self.solde:
                self.solde -= montant
                print(f"Retrait de {montant}. Nouveau solde: {self.solde}")
            else:
                print("Fonds insuffisants.")
        else:
            print("PIN incorrect.")

    def __calculer_interets(self):
        interets = self.solde * 0.05
        self.solde += interets
        print(f"Intérêts de {interets} ajoutés. Nouveau solde: {self.solde}")
# Méthode publique pour accéder à la méthode privée
    def appliquer_interets(self):
        self.__calculer_interets()
# Utilisation
compte = CompteBancaire("Youssouf", 1000)
    