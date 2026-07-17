class programmer():
    comapny = "Microsoft"
    def __init__(self,name,age,Role,Salary):
        self.name = name
        self.age = age
        self.Role = Role
        self.Salary = Salary

w = programmer("Ryujino" , "21", "Developer", "120000")
print(w.name, w.age , w.Role , w.Salary, w.comapny)