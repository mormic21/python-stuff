class Lebewesenen:
    augen = 3

    def __init__(self):
        self.klasse = "säugetier"

    def lebe(self):
        self.augen = 4

class Haustier(Lebewesenen):
    pfoten = 4
    ohren = 3

    def __init__(self):
        self.augen = 4

class Saugetier(Lebewesenen):
    ohren = 2

class Hund(Haustier, Saugetier):
    beine = 42
    name = "bulldogge"

    # konstruktor
    def __init__(self, buchstabeneu='a'):
        Haustier.__init__(self)
        self.buchstabe = buchstabeneu
        self.list = []

    def do_something(self, neuezahl):
        self.augen = neuezahl
        self.lebe()

    def lebe(self):
        Lebewesenen.lebe(self)
        self.beine = 43

if __name__ == '__main__':
    fiffi = Hund()
    #print(Lebewesenen.augen)
    print(fiffi.augen)
    print(fiffi.ohren)