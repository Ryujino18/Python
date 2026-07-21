# class method is a method which is bound to the class and not the objectof theclass
class number():
    a = 1
    @classmethod        #used to create the class method
    def show(cls):
        print(f"The class attribute value is {cls.a}")

e = number()
e.a = 5
e.show()