#Héritage notions
class Animal:
    def ___init__(self, nom, espece):
        self.nom = nom
        self.espece = espece
    def se_deplacer(self):
        return f"{self.nom} se déplace"
    def faire_du_bruit(self):
        return f"{self.nom} fait du bruit"

class Chien(Animal): # Héritage de la classe Animal
    def __init__(self, nom, race):
        super().__init__(nom, 'chien')  # Appel du constructeur de la classe parente
        self.race = race
        def faire_du_bruit(self):  # Surcharge de la méthode faire_du_bruit
            print(f"{self.nom} aboie")
        def remuer_la_queue(self):
            return f"{self.nom} remue la queue"

class Chat(Animal): # Héritage de la classe Animal
    def __init__(self, nom, couleur):
        super().__init__(nom, "Chat")  # Appel du constructeur de la classe parente
        self.couleur = couleur
    def faire_du_bruit(self):  # Surcharge de la méthode faire_du_bruit
        print(f"{self.nom} miaule : Meow!")

# Utilisation
rex = Chien("Rex", "Berger Allemand")
print(rex.remuer_la_queue)  # Rex remue la queue
rex.faire_du_bruit()  # Rex aboie

whiskers = Chat("Whiskers", "Gris")
whiskers.faire_du_bruit()  # Whiskers miaule : Meow!