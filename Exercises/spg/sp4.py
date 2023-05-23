# importerer hele time modulet og hele subprocess modulet
import time, subprocess
# opretter variabel kaldet timeLeft af typen int som holder værdier 3 - kunne kaldes time_left (ifølge pep8 - snake_case)
timeLeft = 3
# opretter listen l som indeholder 5 strenge - kunne kaldes strenge_liste
l= ["Hello","this","is","some","text"]

#definerer funktionen main som tager argumentet a - kunne kaldes print_indhold()
def main(a):
    """ funktionen tager en åben textfil som parameter og printer hver linje
        ved brug af rekursion.
    """
    # line variablen får værdien af første linje fra tekstfilen
    line = a.readline()
    # hvis linjen ikk er tom
    if line:
        #print nuværende linje
        print(line)
        # rekursion - funktionen kalder sig selv indtil der ikke er flere linjer
        return main(a)
#
def wl(a):
    """Itererer over input og skriver det til en tekstfil
    """
    for o in a:
        # skriver elementet o til filen efterfulgt af et linjeskift
        f.write(o + "\n")
    # lukker filen
    f.close()

# åbner filen test.txt og opretter den hvis den ikke findes i forvejen
# argumentet "w" er for at åbne i write mode og sletter indholdet først hvis den findes i forvejen
f = open("test.txt", "w")
# kalder funktionen wl() med listen l som argument
wl(l)
# åbner test.txt filen igen - får default mode 
f = open("test.txt")
main(f)

while timeLeft > 0:
    # end sørger for at der ikke laves linjeskift i print men at der indsættes et whitespace istedet
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1
# kør kommandoen start med argumentet test.txt i shell
# på Windows bruges start til at starte et program og hvis en fil gives som argument åbnes 
# filen med     standardprogrammet til den filtype
subprocess.Popen(['start', 'test.txt'], shell=True)