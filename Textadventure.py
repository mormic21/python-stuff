import random

class Item:
    def __init__(self, weight, worth, name):
        self.weight = weight
        self.worth = worth
        self.name = name

class Potion(Item):
    def __init__(self, weight, worth):
        Item.__init__(self, weight, worth, "Potion")

class HealthPotion(Potion):
    def __init__(self, weight, worth, regenerated_health):
        Potion.__init__(self, weight, worth, "Health")
        self.regenerated_health = regenerated_health

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
        rand = random.randint(0, 6)
        if rand == 0:
            return Field([])
        if rand == 1:
            return Field([])
        if rand == 2 or rand == 3:
            return Field([Ork()])
        if rand == 4 or rand == 5:
            return Field([Goblin(), Goblin(), Ork()])
        if rand == 6:
            return Field([Vader()])

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

def rest(p, m):
    p.rest()

def fight(p, m):
    enemies = m.get_enemies()
    while len(enemies) > 0:
        enemies[0].get_hit(p.ad)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
        for i in enemies:
            p.get_hit(i.ad)
        print("deine hp: " + str(p.hp))

def forward(p, m):
    m.forward()

def backwards(p, m):
    m.backwards()

def right(p, m):
    m.right()

def left(p, m):
    m.left()

def save():
    pass

def load():
    pass

def quit_game(p, m):
    print("Quit!")
    exit(0)

def print_help(p, m):
    print(Commands.keys())

Commands = {
    'help': print_help,
    'quit': quit_game,
    'pickup': pickup,
    'forward': forward,
    'right': right,
    'left': left,
    'backwards': backwards,
    'fight': fight,
    'save': save,
    'load': load,
    'rest': rest,
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