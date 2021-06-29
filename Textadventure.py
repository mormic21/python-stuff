import random

class Item:
    def __init__(self, name):
        self.name = name

class Health(Item):
    def __init__(self):
        Item.__init__(self, "Health")
        self.plushealth = 80

class Sword(Item):
    def __init__(self):
        Item.__init__(self, "Sword")
        self.plusad = 80

class Lightsaber(Item):
    def __init__(self):
        Item.__init__(self, "lightsaber")
        self.plusad = 180

class Shield(Item):
    def __init__(self):
        Item.__init__(self, "shield")
        self.plushealth = 155

class Character:
    def __init__(self, hp, ad, name):
        self.hp = hp
        self.ad = ad
        self.name = name

    def get_hit(self, ad):
        self.hp = self.hp - ad
        if self.hp <= 0:
            self.die()

    def die(self):
        print(self.name + " died")

    def is_dead(self):
        return self.hp <= 0

class Player(Character):
    def __init__(self, name, hp, ad):
        Character.__init__(self, hp, ad, name)
        self.max_hp = hp

    def die(self):
        exit("Verloren")

    def rest(self):
        self.hp = self.max_hp

class Goblin(Character):
    def __init__(self):
        Character.__init__(self, 100, 10, "Goblin")

class Ork(Character):
    def __init__(self):
        Character.__init__(self, 300, 30, "Ork")

class Vader(Character):
    def __init__(self):
        Character.__init__(self, 680, 90, "Darth Vader")

class Field:
    def __init__(self, enemies):
        self.enemies = enemies
        self.loot = []

    def print_state(self):
        print("You look around and see: ")
        for i in self.enemies:
            print(i.name)

    @staticmethod
    def gen_random():
        rand = random.randint(0, 25)
        if rand == 0 or rand == 1 or rand == 2:
            return Field([])
        if rand == 3 or rand == 4:
            return Field([Sword()])
        if rand == 5 or rand == 6 or rand == 7 or rand == 8 or rand == 9:
            return Field([Health()])
        if rand == 10 or rand == 11 or rand == 12 or rand == 13 or rand == 14:
            return Field([Ork()])
        if rand == 15 or rand == 16 or rand == 17 or rand == 18 or rand == 19:
            return Field([Goblin(), Goblin(), Ork()])
        if rand == 20 or rand == 21 or rand == 22:
            return Field([Vader()])
        if rand == 23 or rand == 24:
            return Field([Goblin(), Goblin(), Ork(), Goblin(), Goblin(), Ork(), Lightsaber()])
        if rand == 25:
            return Field([Goblin(), Goblin(), Ork(), Ork(), Vader(), Shield()])

class Map:
    def __init__(self, width, height):
        self.state = []
        self.x = 0
        self.y = 0
        for i in range(width):
            fields = []
            for j in range(height):
                fields.append(Field.gen_random())
            self.state.append(fields)

    def print_state(self):
        self.state[self.x][self.y].print_state()

    def get_enemies(self):
        return self.state[self.x][self.y].enemies

    def forward(self):
        if self.x == len(self.state) - 1:
            print("Ende des Spielfelds")
        else:
            self.x = self.x + 1

    def backwards(self):
        if self.x == 0:
            print("Ende des Spielfelds")
        else:
            self.x = self.x - 1

    def right(self):
        if self.y == len(self.state[self.x]) - 1:
            print("Ende des Spielfelds")
        else:
            self.y = self.y + 1

    def left(self):
        if self.y == 0:
            print("Ende des Spielfelds")
        else:
            self.y = self.y - 1


def pickup(p, m):
    pass

def fight(p, m):
    enemies = m.get_enemies()
    num = len(enemies)
    ok = True
    while len(enemies) > 0:
        if isinstance(enemies[0], Character):
            enemies[0].get_hit(p.ad)
            if enemies[0].is_dead():
                enemies.remove(enemies[0])
                p.ad = p.ad - 10
            for i in enemies:
                p.get_hit(i.ad)
            print("hp: " + str(p.hp) + "; ad: " + str(p.ad))
        else:
            print("Du kannst nicht gegen ein Item kämpfen!")
            ok = False
            break
    if ok:
        p.hp = p.hp + (15 * num)


def forward(p, m):
    m.forward()
    get_koordinates(p, m)

def backwards(p, m):
    m.backwards()
    get_koordinates(p, m)

def right(p, m):
    m.right()
    get_koordinates(p, m)

def left(p, m):
    m.left()
    get_koordinates(p, m)

def save():
    pass

def load():
    pass

def get_hp(p, m):
    print("hp: "+ str(p.hp))

def get_ad(p, m):
    print("ad: "+ str(p.ad))

def get_info(p, m):
    get_hp(p, m)
    get_ad(p, m)

def get_koordinates(p, m):
    print("x: "+str(m.x) + " y: "+str(m.y))

def quit_game(p, m):
    print("Quit!")
    exit(0)

def print_help(p, m):
    print(Commands.keys())

def use_item(p, m):
    enemies = m.get_enemies()
    ok = False
    for i in enemies:
        if isinstance(i, Item):
            if isinstance(i, Health):
                p.hp = p.hp + i.plushealth
                enemies.remove(i)
                print("hp: " + str(p.hp))
                ok = True
            if isinstance(i, Sword):
                p.ad = p.ad + i.plusad
                enemies.remove(i)
                print("ad: " + str(p.ad))
                ok = True
            if isinstance(i, Lightsaber):
                p.ad = p.ad + i.plusad
                enemies.remove(i)
                print("ad: " + str(p.ad))
                ok = True
            if isinstance(i, Shield):
                p.hp = p.hp + i.plushealth
                enemies.remove(i)
                print("hp: " + str(p.hp))
                ok = True
    if not ok:
        print("Kein Nutzbares Item in Sicht")


Commands = {
    'help': print_help,
    'quit': quit_game,
    'hp': get_hp,
    'ad': get_ad,
    'info': get_info,
    #'pickup': pickup,
    'fd': forward,
    'rt': right,
    'lt': left,
    'bs': backwards,
    'fight': fight,
    #'save': save,
    #'load': load,
    'use': use_item
}

if __name__ == '__main__':
    name = input("Enter your name: ")
    p = Player(name, 1000, 100)
    karte = Map(5, 5)
    print("(type help to list the commands available)\n")
    while True:
        command = input(">").lower().split(" ")
        if command[0] in Commands:
            Commands[command[0]](p, karte)
        else:
            print("Befehl nicht gefunden!")
        karte.print_state()