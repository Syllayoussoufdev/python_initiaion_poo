# Visibilité des attributs et méthodes

class CompteBancaire:
    def __init__(self, proprietaire, solde=0, pin="0000"):
        self.proprietaire = proprietaire  # Attribut public
        self._solde = solde  # Attribut public
        self._numero_compte = "123456"  # Attribut protégé
        self.__pin = pin  # Attribut privé

    def voir_solde(self, pin):
        if pin == self.__pin:
            return f"Le Solde de {self.proprietaire} est de : {self._solde} euros."
        else:
            return "PIN incorrect."
    def deposer(self, montant):
        self._solde += montant
        print(f"Dépôt de {montant}. Nouveau solde: {self._solde}")
    
    def retirer(self, montant, pin):
        if pin == self.__pin:
            if montant <= self._solde:
                self._solde -= montant
                print(f"Retrait de {montant}. Nouveau solde: {self._solde}")
            else:
                print("Fonds insuffisants.")
        else:
            print("PIN incorrect.")

    def transferer(self, montant, compte_destinataire, pin):
        if pin == self.__pin:
            if montant <= self._solde:
                self._solde -= montant
                compte_destinataire.deposer(montant)
                print(f"Transféré {montant} à {compte_destinataire.proprietaire}. Nouveau solde: {self._solde}")
            else:
                print("Fonds insuffisants.")
        else:
            print("PIN incorrect.")

    def __calculer_interets(self):
        interets = self._solde * 0.05
        self._solde += interets
        print(f"Intérêts de {interets} ajoutés. Nouveau solde: {self._solde}")
# Méthode publique pour accéder à la méthode privée
    def appliquer_interets(self):
        self.__calculer_interets()
# Utilisation
compteyous = CompteBancaire("Youssouf", 1000, "4321")
compteami = CompteBancaire("Ami", 500, "1234")
compteyous.transferer(200, compteami, "4321")  # Transfert réussi
print(compteyous.voir_solde("2344")) # Accès direct à l'attribut public
print(compteami.voir_solde("1234"))  # Accès direct à l'attribut public

#compteyous.deposer(500)
#compteyous.retirer(200, "1234")  # PIN incorrect

#compteyous.retirer(200, "4321")  # Retrait réussi
#compteyous.appliquer_interets()  # Application des intérêts
#print(compteyous.solde)  # Accès direct à l'attribut public
    