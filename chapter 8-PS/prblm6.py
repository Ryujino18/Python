# write a function to remove a given word from a list and stripit at the same time.

def rem(l,word):
    for item in l:
        l.remove(word)
        return l




l = ["Ryujino", "malware", "an" , "Rohan"]
print(rem(l,"an"))

def rem1(l,word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l = ["Ryujino", "malware", "an" , "Rohan"]
print(rem1(l,"an"))
        



        




