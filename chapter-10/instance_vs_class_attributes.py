class employee:
    language = "c++"        #language, name, slary these are the class attributes
    salary = 120000


Ryujino = employee()                
Ryujino.language = "JavaScript"        #Ryujino is an object attribute or instance attribute
#here the instance attribute takes the preference over the class attributes
print(Ryujino.language, Ryujino.salary)
