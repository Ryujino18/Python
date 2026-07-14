# a= 12
# b= 45
# c= 56

# avg = a+b+c / 3
# print(avg)

# a= 34
# b= 2
# c= 53

# avg1 = a+b+c/3
# print(avg1)


#funtions used to differnetiate
#functions need to be be called outside with the function name to run
def avg(): #function def
    a = int(input("Enter the a value: "))
    b = int(input("Enter the b value: "))
    c = int(input("Enter the c value: "))
    avg1 = a+b+c/3
    print(avg1)
for i in range(5):
    avg()       #function call
    if (i==3):
        print("Thank you!!")
  