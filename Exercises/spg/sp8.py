# Importerer sys-modulen og bruger sys.argv til at hente argumenter, der er givet ved kørslen af scriptet.
# Der er tre argumenter, som er gemt i variablerne s, bi og he, ved hjælp af tuple-unpacking..
import sys
# pass 1 and 2 as argv
s, bi, he = sys.argv
# s er ikke brugt i koden og kan derfor ignoreres.
# bi og he er strengværdier, der er hentet fra sys.argv.

# Først udskrives typen af bi ved hjælp af print(type(bi)).
# Derefter konverteres bi og he til heltal ved hjælp af int()-funktionen og assigneres tilbage til de samme variabler.
print(type(bi))
bi, he = int(bi), int(he)

# main(b, c) funktionen tager to parametre, b og c, og udfører følgende handlinger:

# Beregner produktet af b og c og gemmer resultatet i variablen d.
# Udskriver den binære repræsentation af d ved hjælp af bin()-funktionen.
# Udskriver den heksadesimale repræsentation af d ved hjælp af hex()-funktionen.
# Returnerer værdien af d
def main(b, c):
    d = b * c
    print(bin(d))
    print(hex(d))
    return d

# p() funktionen er defineret uden parametre og udfører følgende handlinger:

# Kalder main() funktionen med bi og he som argumenter og gemmer resultatet i variablen ps.
# Kalder u() funktionen med ps som argument.
def p():
    ps = main(bi, he) 
    u(ps)

# u(pa) funktionen tager et parameter pa og udfører følgende handlinger:

# Initialiserer en variabel i til 10.
# Udfører en løkke, der kører så længe i er større end 0.
# Beregner pa opløftet i i og gemmer resultatet i variablen val.
# Udskriver den decimal repræsentation af val, den binære repræsentation af val og den heksadesimale repræsentation af val.
# Reducerer værdien af i med 1 i hver iteration af løkken.
def u(pa):
    i = 10
    while i > 0:  
        val = pa ** i
        print(f"dec : {val} bin: {bin(val)} hex: {hex(val)}")
        i -= 1

#Til sidst kaldes p() funktionen, hvilket starter udførelsen
# af kodeblokken og resulterer i udskrivning af forskellige repræsentationer og beregninger.
p()