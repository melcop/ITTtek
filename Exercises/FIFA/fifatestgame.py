import random
country = " "
countries = []
# Vi har en list med 4 lande
semifinals = ["Argentina", "Brasil", "France", "Germany"]
# Her har vi længden på listen
sizeofsemifinals = len(semifinals)
#print(sizeofsemifinals)

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
    
    def calculatebestposibility (countries):
        #here you make the algrithm
        return country   
    
    
    
    # No está terminado, tengo que borrar el país elegido para que quede uno menos en la lista
    #semifinals.remove
  
    
print(i)    