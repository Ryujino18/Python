with open("text.txt") as f:
    c = f.read()

with open ("log.txt") as f:
    c1 = f.read()

if (c == c1):
    print("same content")
else:
    print("not same")