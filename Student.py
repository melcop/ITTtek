class Student:
    """A Python class to store student information"""

    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age
        
    def return_name(self):
        """return student name"""
        return self.name

    def return_age(self):
        """return student age"""
        return self.age

    def return_address(self):
        """return student address"""
        return self.address
    
    def update_address(self, address):
        """update student address"""
        self.address = address
        return self.address
        
student1 = Student("John Doe", "Lygten 16, 2400, NV", "29")

print(student1.name)
print(student1.age)
print(student1.address)

student2 = Student("Jane Doe", "123 Main Street, San Jose, CA", "27")

print(student1.update_address("234 Main Street, Newark, CA"))