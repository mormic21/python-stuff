def toKelvin(g):
    return g + 273.15

def getTemp():
    while True:
        c = input("Gib die Temperatur in Celsius ein: ")
        try:
            return float(c)
        except ValueError:
            print("Bitte gültige Zahl eingeben")

if __name__ == "__main__":
    k = toKelvin(getTemp())
    print(str(k) + " Grad Kelvin")