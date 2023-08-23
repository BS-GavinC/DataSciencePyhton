from Persos.Personnage import *
from Spells.Distance import *


class Mage(Personnage, Distance):
    
    def __init__(self, name) -> None:
        Personnage.__init__(self, name)
        Distance.__init__(self)
        self.__mana = 100

    @property
    def mana(self):
        return self.__mana
    
    @mana.setter
    def mana(self, value):
        self.__mana = value

    def attack(self, target):
        if self.mana >= 5:
            super().attack(target)
            self.mana -= 5

    def heal(self, target):
        if self.mana >= 5:
            target.pv += 10
            self.mana -= 5