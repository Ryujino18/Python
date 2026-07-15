#write a program for the list to be cnsored for the givem list

words = ["Donkey", "gande","bahi", "stupid"] 

with open("speech.txt", "r") as f:
    content  = (f.read())
for word in words:
    content = content.replace(word, "#" * len(word))

with open("speech.txt", "w") as f:
    (f.write(content))