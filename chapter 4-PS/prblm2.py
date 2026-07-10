# marks = []
# m1 = int (input ("Enter the mrks:"))
# marks.append(m1)
# m2 = int (input ("Enter the mrks:"))
# marks.append(m2)
# m3 = int (input ("Enter the mrks:"))
# marks.append(m3)
# m4 = int (input ("Enter the mrks:"))
# marks.append(m4)

# marks.sort()
# print(marks)


marks = []

for i in range (6):
    while True:
        try: 
            mark = int(input (f"Enter the marks {i+1}:"))
            marks.append(mark)
            break 
        except ValueError : 
             print("Inavlid crashout")
marks.sort()

print(marks)
