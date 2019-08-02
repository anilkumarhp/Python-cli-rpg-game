from random import randint as ri, sample as sam
from classes.attack import Attack
from classes.potion import Potions
from classes.colors import Colors


class Enemy(Attack, Potions):
    """ Setting up enemy player bot """

    def __init__(self):
        """ Initializing related attributes """
        Attack.__init__(self)
        Potions.__init__(self)
        self.maxhp = 1200  # maxhp for enemy bot remains constant
        self.ehp = 1200  # ehp hp changes based on heal and damage
        self.maxmp = 800
        self.mp = 800
        self.damage = 0
        self.act = 0
        self.attack = 0
        self.count = 0
        self.wturn = 0  # keeping wand turn count
        self.sturn = 0  # keeping spell turn count
        self.maxsp = 5  # max small potion that is available
        self.maxlp = 3  # max large potion that is available
        self.maxfp = 0  # max full potion available
        self.maxmana = 4  # max mana potion that can be stored
        self.fcount = 0  # keep count of full potion received

    def action(self):
        """ used to call the action to perform """
        self.act = 0
        self.count = ri(0, 4)
        if self.count == 0 or self.count == 1 or self.count == 2:
            if self.sturn >= 4:
                if self.wturn <= 3:
                    self.wturn += 1
                self.spellattack(self.sturn)
            elif self.wturn >= 3:
                if self.sturn <= 4:
                    self.sturn += 1
                self.wandattack(self.wturn)
            else:
                if self.wturn <= 3:
                    self.wturn += 1
                if self.sturn <= 4:
                    self.sturn += 1
                self.normalattack()
        elif self.count == 3:
            if self.wturn <= 3:
                self.wturn += 1
            if self.sturn <= 4:
                self.sturn += 1
            self.healing()
        elif self.count == 4:
            if self.wturn < 3:
                self.wturn += 1
            if self.sturn < 4:
                self.sturn += 1
            self.manaheal()

    def normalattack(self):
        """ This is basic attack available in each turn """
        self.act = 1
        sattack = self.weapon_attack()
        print("weapon attack")
        print(f"Damage : {Colors.red}{sattack}{Colors.end}")
        self.damage = sattack

    def wandattack(self, turn):
        """ This is a magic attack performed using Wand """
        self.act = 1
        if self.mana == 0:
            self.normalattack()
        if turn >= 3 and self.mp >= 100:
            self.mp -= 100
            self.wturn = 0
            sattack = self.wand()
            print("wand attack")
            print(f"Damage : {Colors.red}{sattack}{Colors.end}")
            self.damage = sattack
        else:
            self.normalattack()

    def spellattack(self, turn):
        """ This is a magic attack performed using spell """
        self.act = 1
        if self.mana == 0:
            self.normalattack()
        if turn >= 4 and self.mp >= 150:
            self.sturn = 0
            self.mp -= 150
            sattack = self.spell()
            print("spell attack")
            print(f"Damage : {Colors.red}{sattack}{Colors.end}")
            self.damage = sattack
        else:
            self.normalattack()

    def healing(self):
        """ Randomly chooses health from potion class to restore health. """
        if self.ehp >= 900:
            self.manaheal()
        else:
            pot = sam(['S', 'L', 'S', 'L', 'S', 'F', 'S', 'S', 'L', 'F', 'L', 'S', 'L', 'S', 'S'], 1)
            if pot[0] == 'S' and self.maxsp != 0:
                # small potion restores 125 hp
                self.ehp += self.small()
                self.maxsp -= 1
                if self.ehp > self.maxhp:
                    self.ehp = self.maxhp
                print(f"Enemy Healed : {Colors.green}{self.ehp}{Colors.end}")
            elif pot[0] == 'L' and self.maxlp != 0:
                # large potion restores 250 hp
                self.ehp += self.large()
                self.maxlp -= 1
                if self.ehp > self.maxhp:
                    self.ehp = self.maxhp
                print(f"Enemy Healed : {Colors.green}{self.ehp}{Colors.end}")
            elif pot[0] == 'F' and (self.maxfp != 0 or self.ehp < 300):
                # full potion restores full hp
                self.ehp += self.full()
                self.maxfp -= 1
                if self.ehp > self.maxhp:
                    self.ehp = self.maxhp
                print(f"Enemy Healed : {Colors.green}{self.ehp}{Colors.end}")
            else:
                self.normalattack()

    def manaheal(self):
        """  Restore mana used for magic attacks. limit 4 mana per player. """
        if self.mp >= 600:
            if self.ehp >= 900:
                if self.sturn >= 4:
                    self.spellattack(self.sturn)
                elif self.wturn >= 3:
                    self.wandattack(self.wturn)
                else:
                    self.normalattack()
            else:
                self.healing()
        elif self.maxmana != 0:
            self.mp += self.mana()
            self.maxmana -= 1
            if self.mp > self.maxmp:
                self.mp = self.maxmp
            print(f"Mana restored : {Colors.yellow}{self.mp}{Colors.end}")
        else:
            self.normalattack()

    def edamage(self, atk):
        """ Updates hp after each attack by opposite player """
        self.ehp -= atk
        if self.ehp <= 0:
            print(f"{Colors.orange}Hurray!! you  Won :) {Colors.end}")
            exit()

    def getdamage(self):
        """ returns damage """
        if self.act == 1:
            return self.damage
        else:
            return 0

    def status(self):
        return [self.ehp, self.mp]


