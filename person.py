class Person:
    '''This class represents a person object'''

    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

p = Person("Simon", "12344567")
print(p.name)