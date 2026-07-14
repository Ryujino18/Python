#something which calls itself is called as recursion

"""
factorial(0) = 1
factorial(1) = 1 
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factoria (n) = n * factorial (n-1)
"""

def factorial (n):
    if (n == 1 or n == 0):
        return n
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"the factorial of the number {n} is {factorial(n)}")

#need to be cautious while using the recursion

#end="" represents that dont jump to new line continue here only  