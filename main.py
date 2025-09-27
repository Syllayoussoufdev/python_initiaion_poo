class Personne:
    def __init__(self, nom, age, anniv =False):  # Constructeur (__init__ au lieu de __construct)
        self.nom = nom  # self au lieu de $this
        self.age = age
        self.anniv = anniv
    
    def se_presenter(self):
        return f"Je suis {self.nom}, j'ai {self.age} ans"
    
    def Est_Majeur (self):
        if self.age >= 18: return f"Majeur"
        elif self.age >= 65:  return f"Senior"
        else: return f"Mineur"
    
    def avoir_anniversaire(self):
        if self.anniv == True:
            print("Joyeux anniversaire ! Mais tu as déjà fêté ton anniversaire cette année.") 
        else: 
            self.age += 1
            self.anniv = True
            print(f"Joyeux anniversaire ! Maintenant j'ai {self.age} ans")

# Utilisation
alice = Personne("Alice", 25, False)
print(alice.se_presenter())  # Je suis Alice, j'ai 25 
print("je suis donc : " + str(alice.Est_Majeur()))    # Majeur
print("Aujourd'hui est mon anniversaire? ") 
alice.avoir_anniversaire()