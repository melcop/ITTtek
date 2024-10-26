import random
from time import sleep

lives = 9

words = ['pizza', 'fairy', 'shoes', 'tent', 'teeth', 'shirt', 'shirt','otter', 'plane', 'plate']
secret_word = random.choice(words)
print(secret_word)
print("--------------")
words.append('tabel')
print(words)
print(words.index('teeth'))
print("----------------")
print(words.index('tent'))
words.insert(2, 'fork')
print(words)
sleep(2)
words.sort()
print(words)
words.pop(1)
print(words.index('tent'))
words.remove('shoes')
print(words)

if 'tent' in words:
    print('yes')
    words.remove('tent')
else:
    print('no')
print(words)

things = {'apple':1, 'orange':2, 'mango':3}
print(things)
print(things.values())