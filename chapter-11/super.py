class Employee:
    def __init__(self):
        print("Consturctor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Consturctor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__() #super is used to access the methods of a super class in the derived class
        print("Consturctor of Manager")
    c = 3


# o  = Employee()
# print(o.a)  #prints the a attribute

# c = Programmer()
# print(c.b, c.a)  #prints the b attribute and the a attribute


c = Manager()
print(c.b, c.a,c.c)  #prints the b attribute and the a attribute with c attribute 