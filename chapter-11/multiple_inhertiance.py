class Employee():
    company = "ITC"
    name = "Ryujino"
    salary = "1200000"
    def show(self):
        print(f"The Employee name is {self.name} and the salary is {self.salary}")
class coder():
    language = "Python"
    def PrintLanguage(self):
        print(f"Out of all the langauges here is your {self.language} language")

class Programmer(Employee,coder): # basically the employee contents wil be automatically in this programmer class
    company = "ITC ITC"
    def showlang(self):
        print(f"The empoyee {self.name} is proefiecient in this {self.language} language")
a = Employee()
b = Programmer()
print(a.company , b.company)

b.showlang()
b.PrintLanguage()



