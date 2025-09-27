class Personne:
    def __init__(self, nom, age):  # Constructeur (__init__ au lieu de __construct)
        self.nom = nom  # self au lieu de $this
        self.age = age
    
    def se_presenter(self):
        return f"Je suis {self.nom}, j'ai {self.age} ans"
    
    def avoir_anniversaire(self):
        self.age += 1
        print(f"Joyeux anniversaire ! Maintenant j'ai {self.age} ans")

# Utilisation
alice = Personne("Alice", 25)
print(alice.se_presenter())  # Je suis Alice, j'ai 25 ans
alice.avoir_anniversaire()