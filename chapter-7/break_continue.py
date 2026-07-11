# break statement
# used to come out of the loop when encountered, instructs the program to exit the loop
for i in range(100):
    if i == 4:
        break # exit the loop --> here after 4 the loop is exited
    print (i)

# contiue statement
for i in range(100):
    if i == 4:
        continue # skip the iteration -->here 4 will be skipped and rest will be printed
    print (i)