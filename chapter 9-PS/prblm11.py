with open("old.txt") as f:
    c1 = f.read()

with open ("rename_python.txt","w") as f:
    f.write(c1)