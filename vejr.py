vejr = input('Hvordan er vejret i dag? (regn/sne/sol)')

if vejr == 'regn':
    print('Husk paraply!')
elif vejr == 'sne':
    print('Husk handsker og halstørklæde!')
elif vejr == 'sol':
    print('Smukt vejr hvad!')
else:
    print('Du er fucked ;-)!!!')
    print("Pi er = 9,141592 eller hvad?")

i=1
for i in range(15):
    print("Husk at godkende i mTime")
    a = i-15+i*2/2 -i /100
    print(a)
