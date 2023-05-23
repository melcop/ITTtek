# Der oprettes en liste som refereres til med variablen ucl - kunne kaldes unencrypted_list
ucl = []
el = []
d = {"a" : "banana", "b":"apple",
     "c":"orange", "d":"kiwi", "e":"lemon"}

# itererer over strengen abcde
for x in "abcde":
    # x vil have værdien af hvert enkelt bogstav i strengen "abcde"
    # tilføjer values fra alle keys i dictionary d til listen ucl
    ucl.append(d[x])

# funktionen e defineres - kunne kaldes encrypt()
def e():
    """Tilføjer en krypteret version af hvert element i listen ucl
    til og tilføjer dem til listen el.
     """
    # der itereres i en range på længden af items i listen ucl som returneres af len()
    for i in range(len(ucl)):
        # variablen a får værdien af string slicing på item på plads i fra ucl
        # slice statement [::-1] betyder start fra enden af strengen og på position 0
        # ryk med -1 step som betyder ét step tilbage
        # på denne måde omvendes rækkefølgen på bogstaverne i strengen 
        a = ucl[i] [::-1]
        # tiløjer den omvendte streng til listen el
        el.append(a)
    return el

# funktionen ue defineres - kunne kaldes unencrypt()
def ue():
    """Dekrypterer listen el"""
    for i in range(len(el)):
        # string slicing bruges igen til at omvende de omvendte strenge for at dekryptere
        a = el[i] [::-1]
        # her opdateres hvert item i listen el til den dekryptrerede værdi a
        el[i] = a
    return el

# der oprettes en klasse kaldet æ - kunne kaldes tilføj_nøgleværdi()
class æ:
    """Klassen æ har en metode kalde å som tager parametrerne x og y 
    """
    def å(self, y, x):
        """metoden å tjekker om y findes i dictionary d med get funktionen og hvis den returnerer 'Does Not Exist'
    tilføjer den en key med y og en værdi som er strengen x.
    """
        if d.get(y, 'Does Not Exist') == 'Does Not Exist':
            d[y] = str(x)

# der laves en instans af klassen æ
ins = æ()
#metoden å kaldes med argumenterne "f" og "coconut"
ins.å("f", "coconut")
# printer returværdien af funktionen e()
print(e())
# printer returværdien af funktionen ue()
print(ue())