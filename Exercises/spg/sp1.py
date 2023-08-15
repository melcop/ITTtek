# klassen o nedarver fra objekt (moder af alle klasser) kunne kaldes Other
class o(object):
    """Klasse med tre metoder
    ca() printer og returnerer input tallet ganget med 10
    i() printer resultatet af et bolsk udtryk
    a() printer en streng 
    """
    def ca(self, foo):
        """ ca() printer og returnerer input tallet ganget med 10"""
        print(f"val is {foo * 10}")
        return foo * 10
    def i(self):
        """i() printer resultatet af et bolsk udtryk """
        print(f"""{3 != 0.33 or 
        ("func1" != "func2" and True == True)}""")
    def a(self):
        """ a() printer en streng"""
        print("test")
        print("What is this?")
# Klassen c er en komposit med et "has a" relationship som has a "o" Komponent
class c(object):
    """Komposit klasse med en constructor og 3 metoder"""
    def __init__(self):
        """Magic method/ constructor der gør at hver instans af c klassen holder et objekt
        fra o klassen
        """
        self.o = o()
    def i(self):
        """ kalder metoden i() fra instansen af o"""
        self.o.i()
    def ca(self, a):
        """Returnerer input opløftet i 2. modulo 10
        modulo giver restværdien af en division"""
        return  a**2 % 10
    def a(self):
        """printer returværdien af den klassen c's egen metode ca() med inputtet 34.
        Den kalder derefter methoden a() fra komposit komponentet o.
        Til sidst printes en streng som er delt med escape character \n som laver et linebreak"""
        print(f"r = {self.ca(34)}")
        self.o.a()
        print("Composition \nsome stuff after self.o.a()")
# Laver instans af klassen c som refereres til med variablen son
son = c()
# kalder metoden i fra instanse a klassen c
son.i()
# skal printes da man ellers ikke vil se returværdien som output
# 7**2 = 49
# 49 % 10 = 9 
print(son.ca(7))
# kalder objektets metode a()
son.a()