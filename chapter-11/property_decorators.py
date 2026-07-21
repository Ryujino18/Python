# class method is a method which is bound to the class and not the objectof theclass
class number():
    a = 1
    @classmethod        #used to create the class method
    def show(cls):
        print(f"The class attribute value is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = number()
e.a = 5

e.name = "Ryujino Kurosaki"
print(e.name)
