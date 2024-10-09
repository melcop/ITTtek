import random

lives = 9

words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']
secret_word = random.choice(words)
print(secret_word)
print("--------------")
words.append('tabel')
print(words)
print(words.index('teeth'))
print(words.clear())