class CompteBancaire:
    def __init__(self, proprietaire, solde=0, pin="0000"):
        self.proprietaire = proprietaire
        self._solde = solde      # attribut semi-privé (accessible aux enfants)
        self._pin = pin          # attribut protégé

    @property
    def pin(self):
        return self._pin

    def set_pin(self, value):
        self._pin = value
        
    def voir_solde(self, pin):
        if pin == self.pin:
            return f"Solde de {self.proprietaire}: {self._solde} euros"
        else:
            return "PIN incorrect."

    def deposer(self, montant):
        self._solde += montant
        return f"Dépôt de {montant}. Nouveau solde: {self._solde}"

    def retirer(self, montant, pin):
        if pin == self.pin:
            if montant <= self._solde:
                self._solde -= montant
                print(f"Retrait de {montant}. Nouveau solde: {self._solde}")
            else:
                print("Fonds insuffisants.")
        else:
            print("PIN incorrect.")

    def transferer(self, montant, utilisateur, pin):
        if pin == self.pin:
            if montant <= self._solde:
                self._solde -= montant
                print(f"Transféré {montant} du compte de : {self.proprietaire} au compte de  {utilisateur.proprietaire}. Votre Nouveau solde est: {self._solde}")
                utilisateur.deposer(montant)
            else:
                print("Fonds insuffisants.")
        else:
            print("PIN incorrect.")


class CompteEpargne(CompteBancaire):
    def __init__(self, proprietaire, solde=0, pin="0000", taux_interet=0.03):
        super().__init__(proprietaire, solde, pin)
        self._taux_interet = taux_interet

    def calculer_interets(self):
        interets = self._solde * self._taux_interet
        self._solde += interets
        print(f"Intérêts de {interets} ajoutés. Nouveau solde: {self._solde}")

    def retirer(self, montant, pin):
        if pin == self.pin:
            frais = (montant *2)/100    # frais de 2%
            if montant + frais <= self._solde:
                self._solde -= (montant + frais)
                print(f"Retrait de {montant} (+{frais} frais). Nouveau solde: {self._solde}")
            else:
                print("Fonds insuffisants.")
        else:
            print("PIN incorrect.")


class CompteProf(CompteBancaire):
    def __init__(self, proprietaire, solde=0, pin="0000", decouvert_autorise=500):
        super().__init__(proprietaire, solde, pin)
        self._decouvert_autorise = decouvert_autorise

    def retirer(self, montant, pin):
        if pin == self.pin:
            if montant <= self._solde + self._decouvert_autorise:
                self._solde -= montant
                print(f"Retrait de {montant}. Nouveau solde: {self._solde}")
            else:
                print("Fonds insuffisants, même avec découvert autorisé.")
        else:
            print("PIN incorrect.")

# Utilisation
compteyous = CompteProf("Youssouf", 1000, "4321")
compteami = CompteEpargne("Ami", 500, "1234")
compteyous.transferer(200, compteami, "4321")  # Transfert réussi
print(compteyous.voir_solde("4321")) # Accès direct à l'attribut public
print(compteami.voir_solde("1234"))  # Accès direct à l'attribut public