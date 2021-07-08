import random

class Entry:
    def __init__(self, deutsch, englisch):
        self.deutsch = deutsch
        self.englisch = englisch

    def toString(self):
        return self.deutsch + " - " + self.englisch

if __name__ == '__main__':
    eintraege = [Entry("hallo", "hello")]

    def eingabe():
        while True:
            deutsch = input("deutsches Wort: ")
            if deutsch == "#fertig":
                break
            englisch = input("Englisches Wort: ")
            if englisch == "#fertig":
                break
            eintraege.append(Entry(deutsch, englisch))

    def abfrage():
        while True:
            i = random.randint(0, len(eintraege)-1)
            englisch = input("Englisches Wort für: " + eintraege[i].deutsch + ": ")
            if englisch == "#fertig":
                break
            if eintraege[i].englisch == englisch:
                print("korrekt")
            else:
                print("leider Falsch! Richtige Antwort: " + eintraege[i].englisch)

    def printall():
        for i in eintraege:
            print(i.toString())

    while True:
        befehl = input("Befehl: ")
        if befehl == "eingabe":
            eingabe()

        elif befehl == "abfrage":
            abfrage()

        elif befehl == "beenden":
            break

        elif befehl == "ausgabe":
            printall()

        else:
            print("ungueltiger Befehl!")

