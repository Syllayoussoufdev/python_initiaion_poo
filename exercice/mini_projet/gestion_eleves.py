# Classe Etudiant
class Etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = note
    
    def afficher(self):
        print(f"Nom: {self.nom}, Âge: {self.age}, Note: {self.note}")
    
    def est_admis(self):
        return self.note >= 10


# Classe Ecole
class Ecole:
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = []  # liste pour stocker les étudiants
    
    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
    
    def afficher_etudiants(self):
        print(f"--- Étudiants de l'école {self.nom} ---")
        for etu in self.etudiants:
            etu.afficher()
    
    def moyenne_generale(self):
        if len(self.etudiants) == 0:
            return 0
        total = sum([etu.note for etu in self.etudiants])
        return total / len(self.etudiants)


# === Utilisation ===
# Créons une école
mon_ecole = Ecole("Faculté des Sciences")

# Créons des étudiants
etu1 = Etudiant("Ali", 20, 15)
etu2 = Etudiant("Awa", 22, 8)
etu3 = Etudiant("Youssouf", 21, 13)

# Ajoutons-les dans l'école
mon_ecole.ajouter_etudiant(etu1)
mon_ecole.ajouter_etudiant(etu2)
mon_ecole.ajouter_etudiant(etu3)

# Afficher les étudiants
mon_ecole.afficher_etudiants()

# Vérifier si un étudiant est admis
print(f"{etu1.nom} admis ? ", etu1.est_admis())  # True
print(f"{etu2.nom} admis ? ", etu2.est_admis())  # False

# Moyenne générale de l'école
print("Moyenne générale:", mon_ecole.moyenne_generale())
