import random
def some_func(a, b, c=0, d=1):
    return a + b + c + d
result = some_func(1, 2, d=4)
rand_int = random.randint(1, 100)
total = result + rand_int
print(total)