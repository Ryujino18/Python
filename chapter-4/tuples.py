a =()
print(type(a)) # tuple 

a = (1)
print(type(a)) # int

a = (1,)
print(type(a)) # tuple

# a[0] = 1 # not possible
# print(a) # immutable 

a = [10,11,12,13]
a[0] = 1
print(a) # mutable