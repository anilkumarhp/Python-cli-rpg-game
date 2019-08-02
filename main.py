from classes.player import Player
from classes.enemy import Enemy
from random import sample
from classes.colors import Colors


class Game:
    def gstart(self):
        player = Player()
        player.desc()
        enemy = Enemy()
        print(Colors.red+"-"*10+" Enemy's Status "+"-"*10+""+Colors.end, end="  ")
        print(Colors.blue+"-"*10+" Player's Status "+"-"*10+""+Colors.end)
        est = enemy.status()
        pst = player.status()
        print(" "*5, end=" ")
        print(f'{Colors.red}HP : {est[0]} || Mana : {est[1]}' + " "*15+""+Colors.end, end=" ")
        print(f'{Colors.blue}HP : {pst[0]} || Mana : {pst[1]}{Colors.end}')
        print(Colors.red+"-"*36+""+Colors.end, end="  ")
        print(Colors.blue+"-"*37+""+Colors.end)
        print()
        first = sample(["P", "E"], 1)
        if first[0] == "P":
            print("Player Attacks First")
            while True:
                print("--| Player's Turn |--")
                player.action()
                pd = player.getdamage()
                enemy.edamage(pd)
                print()

                print("--| Enemy's Turn |--")
                enemy.action()
                ed = enemy.getdamage()
                player.pdamage(ed)
                print()

                print(Colors.red+"-"*10+" Enemy's Status "+"-"*10+""+Colors.end, end="  ")
                print(Colors.blue+"-"*10+" Player's Status "+"-"*10+""+Colors.end)
                est = enemy.status()
                pst = player.status()
                print(" "*5, end=" ")
                print(f'{Colors.red}HP : {est[0]} || Mana : {est[1]}' + " "*15+""+Colors.end, end=" ")
                print(f'{Colors.blue}HP : {pst[0]} || Mana : {pst[1]}{Colors.end}')
                print(Colors.red+"-"*36+""+Colors.end, end="  ")
                print(Colors.blue+"-"*37+""+Colors.end)
                print()
        elif first[0] == "E":
            print("Enemy Attacks First")
            while True:
                print("--| Enemy's Turn |--")
                enemy.action()
                ed = enemy.getdamage()
                player.pdamage(ed)
                print()

                print(Colors.red+"-"*10+" Enemy's Status "+"-"*10+""+Colors.end, end="  ")
                print(Colors.blue+"-"*10+" Player's Status "+"-"*10+""+Colors.end)
                est = enemy.status()
                pst = player.status()
                print(" "*5, end=" ")
                print(f'{Colors.red}HP : {est[0]} || Mana : {est[1]}' + " "*15+""+Colors.end, end=" ")
                print(f'{Colors.blue}HP : {pst[0]} || Mana : {pst[1]}{Colors.end}')
                print(Colors.red+"-"*36+""+Colors.end, end="  ")
                print(Colors.blue+"-"*37+""+Colors.end)
                print()

                print("--| Player's Turn |--")
                player.action()
                pd = player.getdamage()
                enemy.edamage(pd)
                print()


start = Game()
start.gstart()
