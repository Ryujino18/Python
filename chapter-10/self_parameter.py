class employee:
    language = "c++"        #language, name, slary these are the class attributes
    salary = 120000

    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}.")

    @staticmethod                   #using this there is no req of using self-parameter
    def greet():
        print("Good Morning")


Ryujino = employee()                
Ryujino.language = "JavaScript"        #Ryujino is an object attribute or instance attribute
#here the instance attribute takes the preference over the class attributes
# print(Ryujino.language, Ryujino.salary)
Ryujino.greet()
Ryujino.getinfo()