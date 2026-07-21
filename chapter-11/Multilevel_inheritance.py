class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3


o  = Employee()
print(o.a)  #prints the a attribute
# print(o.b)  # shows error as there is no b attribute in employee class
c = Programmer()
print(c.b, c.a)  #prints the b attribute and the a attribute
c = Manager()
print(c.b, c.a,c.c)  #prints the b attribute and the a attribute with c attribute 