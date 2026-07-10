#program whtehr the given name is present or not in list 

list = ["Black" , "Ryujino" , "Malware", "RRR"]
a = input("Enter the username: ")

if (a in list):
    print(f"This username is in the list and the usernam is {a}")
else:
    print("not there in the list")


#if checking through the list use "in" in the if statement