class Age_Personne : 
    def __init__(self, age):
        self.age = age 
    def Est_Majeur (self):
        if self.age >= 18:
            print("Majeur")
        if self.age >= 65:
            print("Senior")
        else:
            print("Mineur")
age1 = Age_Personne(24)
age1.Est_Majeur()
