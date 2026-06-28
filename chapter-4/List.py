friends = ["Apple", "Orange", 11 , "Ryujino" , False, True]
print (friends[0]) # prints value Apple


friends[0] = "Grapes"
print(friends[0]) # prints Grapes instead of Apples 

# unlike strings lists are mutable
# can store any kind of data in list and is mutubale 
# is accesable using indexing

print(friends[1]) # prints Orange 
print(friends[3]) # prints Ryujino

print(friends[1:3]) # orange and 11 will be printed
