class Item:
    def __init__(self, weight, worth):
        self.weight = weight
        self.worth = worth

class Potion(Item):
    def __init__(self, weight, worth):
        Item.__init__(self, weight, worth)

class HealthPotion(Potion):
    def __init__(self, weight, worth, regenerated_health):
        Potion.__init__(self, weight, worth)
        self.regenerated_health = regenerated_health

class Character:
    def __init__(self, hp, ad):
        self.hp = hp
        self.ad = ad

    def get_hit(self, ad):
        self.hp = self.hp - ad
        if self.ho <= 0:
            self.die()

    def die(self):
        print("Character died")

class Player(Character):
    def __init__(self, name, hp, ad):
        Character.__init__(self, hp, ad)
        self.name = name
        self.max_hp = hp

    def die(self):
        exit("Verloren")

    def rest(self):
        self.hp = self.max_hp

class Goblin(Character):
    def __init__(self):
        Character.__init__(self, 100, 10)

class Ork(Character):
    def __init__(self):
        Character.__init__(self, 300, 30)
class Field:
    def __init__(self, enemies):
        self.enemies = enemies
        self.loot = []

    @staticmethod
    def gen_random():
        pass

class Map:
    def __init__(self, width, height):
        self.state = [[]]
        self.x = 0
        self.y = 0
        for i in range(width):
            fields = []
            for j in range(height):
                fields.append(Field.gen_random())
            self.state.append(fields)

    def print_state(self):
        self.state[self.x][self.y].print_state()

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
    while len(enemies > 0):
        enemies[0].get_hit(p.ad)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
        for i in enemies:
            p.get_hit(i.ad)

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
    map = Map(5, 5)
    print("(type help to list the commands available)\n")
    while True:
        command = input(">").lower().split(" ")
        if command[0] in Commands:
            Commands[command[0]](p, map)
        else:
            print("Befehl nicht gefunden!")
        map.printstate()
