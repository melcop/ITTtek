import random
country = " "
countries = []
# Vi har en list med 4 lande
semifinals = ["Argentina", "Brasil", "France", "Germany"]
# Her har vi længden på listen
sizeofsemifinals = len(semifinals)
#print(sizeofsemifinals)

def calculatebestposibility():
    r = random.randrange(0, 3)
    country = semifinals[r]
    #here you make the algrithm
    return country  


# Este forloop es algoritmo (no está terminado) para elegir que paises se enfrentan
for i in semifinals:
    a = random.randrange(0, sizeofsemifinals)
    b = random.randrange(0, sizeofsemifinals)
    aa = random.randrange(0, sizeofsemifinals)
    bb = random.randrange(0, sizeofsemifinals)
    #print(a, "vs", b)
    c = semifinals[0]
    d = semifinals[1]
    e = semifinals[2]
    f = semifinals[3]
    print(c, a,"vs", b ,d)
    print(e, aa,"vs", bb ,f)

    winners = []

    if a>b:
        winners.append(c)
        print(c,": Winner c!")
    elif b>a:
        print(d, ": Winner d")
        winners.append(d)
    else:
        print("Draw. Only 1 point!")

    if aa>bb:
        winners.append(e)
        print(e, ": Winner e")
    elif bb>aa:
        winners.append(f)
        print(f, ": Winner f")
    else:
        print("Draw")
 
#print(calculatebestposibility(), ": Top 10 FIFA RANKING LIST")
    
    
    # No está terminado, tengo que borrar el país elegido para que quede uno menos en la lista
    #semifinals.remove
print(winners) 
r = random.randrange(0, 3)
s1 = winners[0]
s2 = winners[1]
r1 = random.randrange(5)
r2 = random.randrange(5)
print(s1, r1,"vs", r2 ,s2)
if r1>r2:
    print("winner is: ", s1)
elif r2>r1:
    print("winner is: ", s2)
print()
print("Perfect game. Go!")    