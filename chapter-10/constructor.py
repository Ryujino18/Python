class employee:
    language = "c++"        #language, name, slary these are the class attributes
    salary = 120000

    def __init__(self, name, salary , langauge): #dunder method which is automatically called
        self.name = name
        self.language = langauge
        self.salary = salary
        print("I m creating an obj")

    def getinfo(self):
        print(f"i'm {self.name} and The language is {self.language} and the salary is {self.salary}.")

    @staticmethod                   #using this there is no req of using self-parameter
    def greet():
        print("Good Morning")


Ryujino = employee("Ryujino", 120000, "Js")      #You need to enter the parameters if you are using the init function          
# Ryujino.language = "JavaScript"        #Ryujino is an object attribute or instance attribute
# Ryujino.greet()
# Ryujino.getinfo()
print(Ryujino.name , Ryujino.salary, Ryujino.language)