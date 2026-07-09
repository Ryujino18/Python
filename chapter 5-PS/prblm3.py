d={}
for i in range(5):
    name = input("Enter your name:")
    lang = input("Enter language:")
    d.update({name : lang})
print(d)
#if keys are same then the latest one will be used
# if values are same then no prblm

# we cannot add list to set, cant change the texts using indexing