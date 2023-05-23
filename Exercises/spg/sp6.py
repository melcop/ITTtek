class p(object):
    """Er parent til c og Klassen har 3 metoder"""
    def x(self, n):
        return n * 2
    def y(self):
        print("PARENT y")
    # z har type hints der giver et bud på typen af parameter, 
    # men giver ikke fejl hvis en anden type indsættes
    def z(self, foo : str = "not given" , bar: int = 999):
        """Returnerer en f-string med inputparameteret foo som skal være en string,
        
        og det unicode symbol som er mapped til inputparameteret bar som skal være af typen int
        """
        return f"{foo}  \n {chr(bar)}"

class c(p):
    """Klassen nedarver z() metoden fra p klassen og overskriver x og y metoderne"""
    # overskriver funktionen x som der var nedarvet, ved at få samme navn
    def x(self, n):
        return n / 2
    def y(self):
        print(self.x(15))
        # Super funktionen kalder den oprindelige metode fra base-klassen selvom den er overskrevet
        super(c, self).y()
        print("super duper")

# laver instans af klassen p som refereres til med variablen d - kunne kaldes dad
d = p()
# laver instans af klassen c som refereres til med variablen s - kunne kaldes son
s = c()
# kalder y metoden
d.y()
# kalder den overskrevne y metode
s.y()
d.x(10)
# returnerer 40 men vises ikke da det ikke printes
s.x(20)
# kalder z metoden fra d instansen
print(d.z("char enc:", 127773))
# kalder z metoden fra s instansen som har nedarvet den fra p klassen
print(s.z("number ?? is:", 127774))