import random

lives = 9

words = ['pizza', 'fairy', 'shoes', 'tent', 'teeth', 'shirt', 'otter', 'plane', 'plate']
secret_word = random.choice(words)
print(secret_word)
print("--------------")
words.append('tabel')
print(words)
print(words.index('teeth'))