import random
from time import sleep

lives = 9

words = ['pizza', 'hotdog','fairy', 'shoes', 'tent', 'teeth', 'shirt', 'shirt','otter', 'plane', 'plate','hat']
secret_word = random.choice(words)
print(secret_word)
print("--------------")
words.append('tabel')
print(words)
print(words.index('teeth'))
print("----------------")
print(words.index('tent'))
words.insert(2, 'forko')
print(words)
sleep(2)
words.sort()
print(words)
words.pop(1)
print(words.index('tent'))
words.remove('hotdog')
print(words)

if 'tent' in words:
    print('yes')
    words.remove('tent')
else:
    print('no')
print(words)

things = {'apple':1, 'orange':2, 'mango':3, 'banana':4}
print(things)
print(things.values())
print(things.get('apple'))
a = 3, 14159212, 2
b = 3.42
print(a.index(2)+b)