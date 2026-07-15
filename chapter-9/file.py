#A file is a data stored in a storage device. A python program can read it by reading the content from it and writing content to it.
#rb - read in binary
#rt - read in text
#w - write
#r - read
#a - append
f = open("file.txt" , "rb")
data = f.read()
print(data)
f.close()