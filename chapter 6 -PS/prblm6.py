#grading system

marks = int(input ("Enter the marks:"))

if (marks<=100 and marks >=90):
    Grade = "O"
elif (marks<90 and marks >=80):
    Grade = "A"
elif (marks<80 and marks >=70):
    Grade = "B"
elif (marks<70 and marks >=60):
    Grade ="C"
elif (marks<60 and marks >=50):
    Grade ="D"
else: 
    print("fail")

print(f"Your grade is {Grade}")