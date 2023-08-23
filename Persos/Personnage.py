

class Personnage:

    def __init__(self, name) -> None:
        self.__name = name
        self.__pv = 100

    @property
    def pv(self):
        return self.__pv
    
    @property
    def name(self):
        return self.__name
    
    @pv.setter
    def pv(self, value):
        self.__pv = value

    def attack(self, target):
        target.pv -= 20