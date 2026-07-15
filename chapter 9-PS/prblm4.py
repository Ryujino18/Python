# write a python program to change the word Donkey to #### (update)
word = "Donkey" 

with open("text.txt", "r") as f:
    c  = (f.read())

contentNew = c.replace(word, "#####")

with open("text.txt", "w") as f:
    (f.write(contentNew))

