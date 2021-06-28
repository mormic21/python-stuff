class MyClass:
    zahl = 15
    string = "zeichenkette"

    #konstruktor
    def __init__(self, buchstabeneu='a'):
        self.buchstabe = buchstabeneu

    def do_something(self, neuezahl):
        self.zahl = neuezahl


if __name__ == '__main__':
    instanz = MyClass('z')
    instanz2 = MyClass('b')
    print(instanz.buchstabe)
    print(instanz.string)
    print(MyClass.string)
    instanz.string = "42"
    print(instanz.string)
    print("------")
    print(instanz.zahl)
    instanz.do_something(1337)
    print(instanz.zahl)