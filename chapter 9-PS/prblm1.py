#write a code where it has to read hte file and 
#check whether it has the content in it or not
with open("poem.txt") as f:
     c = (f.read())

print(c)

if ("Twinkle" in c):
    print("Twinkle is present in the content!!")
else:
    print("Twinkle is not present in the content!!")
