# recusrsive function to calculate the sum of first n numbers

def sum(n):
    i = 0
    sum = 0
    for i in range(0,n+1):
        sum += i
        i = i+1
    return sum
n = int(input ("Enter a number: "))

print(sum(n))

#using recursion
"""
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
sum(n) = sum(n-1) + n
"""

def sum(n):
    for i in range(0,n+1):

        if (n==1 or n==0):
            return 1
        else:
            return sum(n-1) + n
        
print(sum(5))