name = "rYujino"
print(len(name)) #6
print (name.endswith("no")) #True
print(name.startswith("yu")) #False
print(name.capitalize()) #Capitalize first letter
print (name.lower()) # all Small
print(name.upper()) # all capital
print(name.title()) #capitalizes the first capater of each word

n = "Hello World"
print(n.find('World')) #index of the first occurence of the word in the string

print(n.replace ("Hello" , "Hi"))

#strips 

s = " hi hello "
print(s.strip()) # removes leading and trailing white spaces
print(s.lstrip()) # removes leading space
print(s.rstrip()) # removes tailing space

print(s.alnum())#true - checks if any number and alphabet is there or not
print(s.isalpha) #true - checks if it has only alpha
print(s.isdigit) #false - cels if all the characetrs are digit