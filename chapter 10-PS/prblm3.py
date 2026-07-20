class Demo:
    a = 5

object = Demo()
print(object.a) # prints class attribute because instance attribute is not present
object.a = 1 # instance attribute is set
print(object.a) # prints instance attribute becuase instance attribute is present
print(Demo.a) # prints class attribute