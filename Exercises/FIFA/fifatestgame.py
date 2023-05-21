import random

# Vi har en list med 4 lande
semifinals = ["Argentina", "Brasil", "France", "Germany"]
# Her har vi længden på listen
sizeofsemifinals = len(semifinals)
#print(sizeofsemifinals)

# Este forloop es algoritmo (no está terminado) para elegir que paises se enfrentan
for i in semifinals:
    a = random.randrange(0, sizeofsemifinals)
    b = random.randrange(0, sizeofsemifinals)
    #print(a, "vs", b)
    c = semifinals[0]
    d = semifinals[1]
    print(c, a,"vs", b ,d)
    
    # No está terminado, tengo que borrar el país elegido para que quede uno menos en la lista
    #semifinals.remove
  
    
print(i)    