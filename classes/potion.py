class Potions:
    """ provides potions used in the game """

    def __init__(self):
        """ Initialize the potions """
        self.smallp = 125
        self.largep = 250
        self.fullp = 1200
        self.manap = 200

    def small(self):
        """ returns small potion """
        return self.smallp

    def large(self):
        """ returns large potion """
        return self.largep

    def full(self):
        """ returns full potion """
        return self.fullp

    def mana(self):
        """ returns magic potion (mana) """
        return self.manap

