#calculator builder for square and cubes

class calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(self.n*self.n)

    def cube(self):
        print(self.n^3)
n = int(input("Enter a number:"))
a = calculator(n)
a.square()
a.cube()