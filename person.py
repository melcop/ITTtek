class Person:
    '''This class represents a person object'''

    def __init__(self, first_name, surname, tel):
        self.first_name = first_name
        self.surname = surname
        self.tel = tel

    def full_name(self):
        return self.first_name + " " + self.surname

p = Person("Simon", "Nielsen", "12344567")
print(p.first_name)
print(p.surname)