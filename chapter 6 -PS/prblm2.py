# student pass or fail , pass = 40% and atleast 33% in each subject

a = int(input ("Enter marks:"))
b = int(input ("Enter marks:"))
c = int(input ("Enter marks:"))

total_percent = ((a+b+c)*100)/300

if (total_percent>=40 and a>33 and b>33 and c>33):
    print(f"You are passed: {total_percent}")

else:
    print(f"You failed {total_percent}")