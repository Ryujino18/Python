# whetehr the charcters are less then 10 or not

a = input("Enter a name: ")
b = len(a)

print(f"characters in the name is  {b}")

if (b>10):
    print(f"characters are greater than 10, i.e is {b}")
else:
    print(f"characters are lesser than 10, i.e is {b}")