from Persos.Personnage import *

class Nain(Personnage):

    def __init__(self, name) -> None:
        super().__init__(name)
        self.__force = 25

    @property
    def force(self):
        return self.__force
    
    @force.setter
    def force(self, value):
        self.__force = value

    def boire(self):
        self.pv += 15
        self.force -= 5