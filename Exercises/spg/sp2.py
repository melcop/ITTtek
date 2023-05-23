# importerer datetime klassen fra datetime modulet
from datetime import datetime
# importerer sleep funktionen fra time modulet
from time import sleep

# der oprettes en liste som refereres til med variablen l
l = []
# der oprettes en dictionary som refereres til med variablen d
d = {}

# funktionen c() defineres
# kunne kaldes udregn_regning_med_drikkepenge()
def c(b, tp=10):
    """Funktionen c tager input b og eventuelt tp som ellers som default vil være 10.

    b er beløbet på regningen og tp er hvor mange procentaf beløbet, der skal gives i drikkepenge.

    Det udregnede beløb printes i en f-string inden det returneres.
    """
    # Burde være 0.01 for at lægge 10% oven i beløbet
    t = b*(1+0.1 * tp)
    # afrunder tallet med 2 decimaler
    t = round(t, 2)
    print(f"t ={t}")
    return t

# nested loop, The "inner loop" will be executed one time for each iteration of the "outer loop":
# Nested loop - den "indre løkke" vil blive eksekveret én gang for hver iteration af den "ydre løkke"
# loopet itererer i en range fra 1 til 4 (non inclusive)
for i in range(1, 4):
    # tilføjer returværdien fra c() til listen l
    l.append(c(i+0.334546))
    # printer listen l og for loop variablen i
    print(l,"\n", i, "\n")
    
    # hele dette loop køres for hver iteration af det ydre loop
    for j in range(1, 4):
        # tilføjer returværdien fra datatime.now som key og value er listen l til dictionary d
        d[str(datetime.now())] = l
        print("j", j, "\n", d)
        sleep(0.1)