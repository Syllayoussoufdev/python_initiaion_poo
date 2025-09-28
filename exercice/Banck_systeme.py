#Objectif : Gérer des comptes bancaires avec héritage
class CompteBancaire:
    def __init__(self, proprietaire, solde=0, pin="0000"):
        self.proprietaire = proprietaire  # Attribut public
        self.__solde = solde  # Attribut privé
        self._pin = pin  # Attribut privé

    def set_pin(self, value):
        self._pin = value
    
    # Getter pour l'attribut privé __pin
    @property
    def get_pin(self):
        return self._pin

    def voir_solde(self, pin):
        if pin == self.get_pin:
            return print(f"Le Solde de {self.proprietaire} est de : {self.__solde} euros.")
        else:
            return "PIN incorrect."
        
    def deposer(self, montant):
        self.__solde += montant
        print(f"Dépôt de {montant}. Nouveau solde: {self.__solde}")

    def retirer(self, montant, pin):
        if pin == self.get_pin:
            if montant <= self.__solde:
                self.__solde -= montant
                print(f"Retrait de {montant}. Nouveau solde: {self.__solde}")
            else:
                print("Fonds insuffisants.")
        else:
            print(f"PIN incorrect.")

    def transferer(self, montant, compte_destinataire, pin):
        if pin == self.get_pin:
            if montant <= self.__solde:
                self.__solde -= montant
                compte_destinataire.deposer(montant)
                print(f"Transféré {montant} à {compte_destinataire.proprietaire}. Nouveau solde: {self.__solde}")
            else:
                print("Fonds insuffisants.")
        
        else:
            print("PIN incorrect.")


class CompteEpargne(CompteBancaire):
    def __init__(self, proprietaire, solde=0, pin="0000", taux_interet=0.03):
        super().__init__(proprietaire, solde, pin,)
        self.__taux_interet = taux_interet  # Attribut privé

        def Calculer_interets(self):
            interets = self.__solde * self.__taux_interet
            self.__solde += interets
            print(f"Intérêts de {interets} ajoutés. Nouveau solde: {self.__solde}")
        
        def retirer(self, montant, pin):
            if pin == self.get_pin:
                if montant <= self.__solde:
                    self.__solde -= (montant + montant * 2)  # Frais de 2 pour les retraits
                    print(f"Retrait de {montant}. Nouveau solde: {self.__solde}")
            else:
                print(f"PIN incorrect.")

class Compte_Prof(CompteBancaire):
    def __init__(self, proprietaire, solde=0, pin="0000", decouvert_autorise=500):
        super().__init__(proprietaire, solde, pin)
        self.__decouvert_autorise = decouvert_autorise  # Attribut privé

    def retirer(self, montant, pin):
        if pin == self.get_pin:
            if montant <= self.__solde + self.__decouvert_autorise:
                self.__solde -= montant
                print(f"Retrait de {montant}. Nouveau solde: {self.__solde}")
            else:
                print("Fonds insuffisants, même avec le découvert autorisé.")
        else:
            print(f"PIN incorrect.")

# Utilisation
compteyous = Compte_Prof("Youssouf", 1000, "4321")
compteyous.voir_solde("4321")
compteami = CompteEpargne("Ami", 500, "1234")
compteami.voir_solde("1234")

compteyous.transferer(200, compteami, "4321")  # Transfert réussi
compteyous.voir_solde("4321") # Accès direct à l'attribut public
compteyous.retirer(1300, "4321")  # Retrait avec découvert autorisé
compteyous.voir_solde("4321") # Accès direct à l'at