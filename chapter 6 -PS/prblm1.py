# greatest of four numbers
'''

for i in range(4):
    a = int(input(f"Enter the number {i+1}:"))

if (a>a+1 and a>a+2 and a>a+3):
    print(f"{a} is greatest number")
elif (a+1>a and a+1>a+2 and a+2>a+3):
    print(f"{a+1} is greatest number")
elif (a+2>a and a+2>a+1 and a+2>a+3):
    print(f"{a+3}is the greatest number")
else: 
    print(f"{a+4} is the greatest number")

'''

a = int(input("Enter a number:"))
a1 = int (input ("Enter a number: "))
a2 = int(input("Enter a number:"))
a3 = int (input ("Enter a number: "))

if (a>a1 and a>a2 and a>a3):
    print(f"{a} is the greatest")
elif (a1>a and a1>a2 and a1>a3):
    print(f"{a1} is the greatest")
elif (a2>a and a2>a1 and a2>a3):
    print(f"{a2} is the greatest")
else: 
    print(f"{a3} is the greatest number")