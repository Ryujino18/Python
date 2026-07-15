# f= open("myfile.txt")
# print(f.open())
# f.close()

#smae can be used written using with statemnt like this
with open("file.txt") as f:
    print(f.read())
#you dont have to close the file