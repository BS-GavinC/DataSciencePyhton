# Creez une classe User qui a comme attribut private Nom Prenom 
# et Age. User("jean", "pol", 42)
# Definissez deux Getter (property) , un qui va renvoyer 
# "Nom + Prenom" et un qui va renvoyer l'age
# Definissez un setter sur l'age, seulement si la valeur 
# rentrée est inferieur à zero ou superieur a 100, doit 
# maintenir l'age dans ce range.

class User:

    def __init__(self, fName, lName, age):
        self.__firstname = fName.capitalize()
        self.__lastname = lName.capitalize()
        self.__age = self.__gap_age(age)

    @property
    def nom_complet(self):
        return self.__firstname + " " + self.__lastname
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = self.__gap_age(value)

    

    def __gap_age(self, age):
        return 0 if age <= 0 else 100 if age > 100 else age