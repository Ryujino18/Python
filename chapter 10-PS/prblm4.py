class calculator:

    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(self.n*self.n)
    
    def cube(self):
        print(self.n*self.n*self.n)
    
    def squareroot(self):
        print(self.n**1/2)

    @staticmethod
    def greet():
        print("Hello world")
    
n = int(input("Enter a number:"))
a = calculator(n)
a.square()
a.cube()
a.squareroot()
a.greet()