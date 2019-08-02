from random import randint as ri, sample as sam
from classes.attack import Attack
from classes.potion import Potions
from classes.colors import Colors
from sys import exit


class Player(Attack, Potions):
    """ Setting up enemy player bot """

    def __init__(self):
        """ Initializing related values """
        Attack.__init__(self)
        Potions.__init__(self)
        self.damage = 0
        self.act = 0
        self.maxhp = 1200
        self.php = 1200
        self.maxmp = 800
        self.mp = 800
        self.attack = 0
        self.count = 0
        self.wturn = 0  # keeping wand turn count
        self.sturn = 0  # keeping spell turn count
        self.maxsp = 5  # max small potion that can be stored
        self.maxlp = 3  # max large potion that can be stored
        self.maxfp = 0  # max full potion available
        self.maxmana = 4  # max mana potion that can be stored
        self.fcount = 0  # keep count of full potion received
        self.choice = []
        self.fpcount = 0

    def desc(self):
        print("Your options")
        print("""
            1. Basic attack (min damage 50), available every turn
            2. wand attack (min damage 75), available after each 2nd turn
            3. spell attack (min damage 100), available after each 3rd turn
            4. Healing health, available only when health is less than max .
            5. Mana restore, available when mana is not full.  
        """)

    def action(self):
        """ used to call the action to perform """
        self.choice = [1]
        self.act = 0
        print("Available options")
        print("1 : Basic Attack")
        if self.wturn >= 3 and self.mp >= 100:
            self.choice.append(2)
            print("2 : Wand Attack")
        if self.sturn >= 4 and self.mp >= 150:
            self.choice.append(3)
            print("3 : Spell Attack")
        if (self.maxlp != 0 or self.maxfp != 0 or self.maxsp != 0) and self.php != self.maxhp:
            self.choice.append(4)
            print("4 : Healing health")
        if self.mp != self.maxmp and self.maxmana >= 0:
            self.choice.append(5)
            print("5 : Mana restore")

        while True:
            print("Enter :")
            choice = int(input())
            try:
                self.choice.index(choice)
            except ValueError:
                print(f'{choice} is not a valid option')
                print("try Again!!")
                continue
            if choice == 1:
                if self.wturn <= 3:
                    self.wturn += 1
                if self.sturn <= 4:
                    self.sturn += 1
                self.normalattack()
            elif choice == 2:
                if self.sturn <= 4:
                     self.sturn += 1
                self.wandattack(self.wturn)
            elif choice == 3:
                if self.wturn <= 3:
                    self.wturn += 1
                self.spellattack(self.sturn)
            elif choice == 4:
                if self.wturn <= 3:
                    self.wturn += 1
                if self.sturn <= 4:
                    self.sturn += 1
                while True:
                    print("Healing Potions Available")
                    if self.maxsp > 0:
                        print(f'     1 : Small potion - {self.maxsp}')

                    if self.maxlp > 0:
                        print(f'     2 : Large potion - {self.maxlp}')

                    if self.maxfp > 0:
                        print(f'     3 : Full potion - {self.maxfp}')

                    print("Enter : ")
                    ch = int(input())
                    if ch == 1:
                        self.smallpotion()
                    elif ch == 2:
                        self.largepotion()
                    elif ch == 3:
                        self.fullpotion()
                    else:
                        print(f'Invalid choice {ch}')
                        print("Try again!!")
                        continue
                    break
            elif choice == 5:
                if self.wturn < 3:
                    self.wturn += 1
                if self.sturn < 4:
                    self.sturn += 1
                self.manaheal()
            else:
                print(f'Invalid choice {choice}')
                print("Try Again!!")
                continue
            break

    def normalattack(self):
        self.act = 1
        sattack = self.weapon_attack()
        print(f"Damage : {Colors.red}{sattack}{Colors.end}")
        self.damage = sattack

    def wandattack(self, turn):
        self.act = 1
        if turn >= 3 and self.mp >= 100:
            self.mp -= 100
            self.wturn = 0
            sattack = self.wand()
            print("wand attack")
            print(f"Damage : {Colors.red}{sattack}{Colors.end}")
            self.damage = sattack
            if self.damage >= 280 and self.fpcount == 0:
                self.maxfp += 1
                self.fpcount = 1
                print("Hurray!!! you got a item!\nFull health potion!!")

        else:
            self.normalattack()

    def spellattack(self, turn):
        self.act = 1
        if turn >= 4 and self.mp >= 150:
            self.mp -= 150
            self.sturn = 0
            sattack = self.spell()
            print("spell attack")
            print(f"Damage : {Colors.red}{sattack}{Colors.end}")
            self.damage = sattack
            if self.damage >= 250 and self.fpcount == 0:
                self.maxfp += 1
                self.fpcount = 1
                print("Hurray!!! you got a item!\nFull health potion!!")
        else:
            self.normalattack()

    def smallpotion(self):
        self.php += self.small()
        self.maxsp -= 1
        if self.php > self.maxhp:
            self.php = self.maxhp
        print(f"Player Healed : {Colors.green}{self.php}{Colors.end}")

    def largepotion(self):
        self.php += self.large()
        self.maxlp -= 1
        if self.php > self.maxhp:
            self.php = self.maxhp
        print(f"Player Healed : {Colors.green}{self.php}{Colors.end}")

    def fullpotion(self):
        self.php += self.full()
        self.maxfp -= 1
        if self.php > self.maxhp:
            self.php = self.maxhp
        print(f"Player Healed : {Colors.green}{self.php}{Colors.end}")

    def manaheal(self):
        """
            Methods too restore mana used for magic attacks.
            limit 4 mana per player.
        """
        self.maxmana -= 1
        self.mp += self.mana()
        if self.mp > self.maxmp:
           self.mp = self.maxmp
        print(f"Mana restored : {Colors.yellow}{self.mp}{Colors.end}")

    def pdamage(self, atk):
        self.php -= atk
        if self.php <= 0:
            print(f"{Colors.black} Enemy Won :( {Colors.end}")
            exit()

    def getdamage(self):
        if self.act == 1:
            return self.damage
        else:
            return 0

    def status(self):
        return [self.php, self.mp]
