a= int(input("Enter age:"))

# if statement no.1
if(a%2 == 0):
    print("a is even")

    
# if statement no.2
if (a>=18):
    print("you are above 18")
elif (a<0):
    print("You cannot enter negative age")
elif (a>150): 
    print("Enter a valid age")
else:
    print("you are below 18")

print("I'm done")
