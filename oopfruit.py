class Fruit:
    def __init__(self):
        print('1')

class Apple(Fruit):
    def __init__(self):
        print('2')
print("test3")
obj = Apple()
c= 12
print(c)
magic = []
magic.append(c)
magic.append(Apple)
print(magic)