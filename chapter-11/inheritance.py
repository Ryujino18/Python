class Employee():
    company = "ITC"
    def show(self):
        print(f"The Employee name is {self.name} and the salary is {self.salary}")

# class Programmer():
#     company = "ITC infotech"
#     def show(self):
#         print(f"The Employee name is {self.name} and the salary is {self.salary}")
#     def showlang(self):
#         print(f"The empoyee {self.name} is proefiecient in this {self.language} language")

#This holds good when there is no need of changing anything, if yu have t change the class Employee then you have to start form the change and change everything

#Due to which inheritance concept comes in

class Programmer(Employee): # basically the employee contents wil be automatically in this programmer class
    company = "ITC ITC"
    def showlang(self):
        print(f"The empoyee {self.name} is proefiecient in this {self.language} language")
a = Employee()
b = Programmer()
print(a.company , b.company)



#inheritance is a ways of creating a new class from an existing class