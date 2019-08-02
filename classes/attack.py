from random import randrange as r


class Attack:

    def __init__(self):
        self.atk = 0
        self.watk = 0
        self.matk = 0

    def magic_attack(self):
        return r(0, 200, 20)

    def weapon_attack(self):
        self.watk = 75 + r(0, 100, 10)
        return self.watk

    def wand(self):
        self.matk = 100 + self.magic_attack()
        return self.matk

    def spell(self):
        self.matk = 150 + self.magic_attack()
        return self.matk

