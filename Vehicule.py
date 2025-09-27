class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self._kilometrage = 0
    
    @property
    def kilometrage(self):
        return self._kilometrage
    
    def rouler(self, distance):
        self._kilometrage += distance
        print(f"Le véhicule a roulé {distance} km. Total: {self._kilometrage} km")
    
    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee}) - {self._kilometrage} km"

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, nb_portes):
        super().__init__(marque, modele, annee)
        self.nb_portes = nb_portes
        self._reservoir = 50  # Litres
    
    def faire_le_plein(self):
        self._reservoir = 50
        print("Réservoir plein !")
    
    def rouler(self, distance):  # Override avec logique supplémentaire
        if self._reservoir > 0:
            super().rouler(distance)
            self._reservoir -= distance / 10  # Consommation simplifiée
            if self._reservoir < 0:
                self._reservoir = 0
        else:
            print("Plus d'essence !")

# Utilisation
ma_voiture = Voiture("Toyota", "Corolla", 2020, 4)
ma_voiture.rouler(100)
print(ma_voiture)  # Toyota Corolla (2020) - 100 km
ma_voiture.faire_le_plein()