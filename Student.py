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

print("Name: ", student1.name)
print("Age: ", student1.age)
print("Address: ", student1.address, "\n")

print("----------------------------\n")

print("Person1: ",student1.name, student1.age, student1.address,"\n")

student2 = Student("Jane Doe", "123 Main Street, San Jose, CA", "27")


student1.update_address("234 Main Street, Newark, CA")

print("After update ", "----------------------------", "After update \n")

print("Person1: ",student1.name, student1.age, student1.address)

print("-----------------------------------------------------\n")

print("Person2: ",student2.name, student2.age, student2.address)