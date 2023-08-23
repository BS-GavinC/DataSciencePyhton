from Persos.Personnage import *

class Chasseur(Personnage):

    def __init__(self, name) -> None:
        super().__init__(name)
        self.__nbr_fleche = 12

    @property
    def nbr_fleche(self):
        return self.__nbr_fleche
    
    @nbr_fleche.setter
    def nbr_fleche(self, value):
        self.__nbr_fleche = value