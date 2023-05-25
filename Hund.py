class Hund:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    def bark(self):
        print("Vov!")
        
    def happy(self):
        print("O-O")

# Opret en instans af klassen Hund
min_hund = Hund("Fido", 3)

# Brug metoden bark på instansen
min_hund.bark()
# Glad hund
min_hund.happy()