#Objectif : Créer une classe Livre simple
class livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.titre = titre # Titre du livre
        self.auteur = auteur # Auteur du livre
        self.nombre_de_pages = nombre_de_pages # Nombre total de pages
        self.page_courante = 0 # Page actuelle
        self.lu = False # Indique si le livre a été lu ou non

    def lire(self, pages):
        self.lu = True
        if self.page_courante + pages >= self.nombre_de_pages:
            self.page_courante = self.nombre_de_pages
            print(f"Vous avez fini de lire '{self.titre}' de {self.auteur}.")
        else:
            self.page_courante += pages
            print(f"Vous avez lu {pages} pages. Vous êtes maintenant à la page {self.page_courante}.")

    def aller_a_la_page(self, page):
        if 0 <= page <= self.nombre_de_pages:
            self.page_courante = page
            print(f"Vous êtes maintenant à la page {self.page_courante} de '{self.titre}'.")
        else:
            print("Numéro de page invalide.")
    
    def info(self):
        statut = "lu" if self.lu else "non lu"
        return f"'{self.titre}' par {self.auteur}, {self.nombre_de_pages} pages, page actuelle: {self.page_courante}, statut: {statut}"

    def __str__(self):
        return f"'{self.titre}' par {self.auteur}, {self.nombre_de_pages} pages"

# Utilisation
livre1 = livre("CODAGE INFORMATIQUE", "SYLLA YOUSSOUF", 328)
print(livre1)  # Affiche les informations du livre
livre1.lire(50)  # Lire 50 pages
livre1.aller_a_la_page(100)  # Aller à la page 100
print(livre1.info())  # Affiche les informations détaillées du livre
