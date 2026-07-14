# inches to cm

def inch_to_cms(inch):
    return inch * 2.54
inch = int(input ("Enter the number: "))
cm = inch_to_cms(inch)
print(f"{inch} in cm = {round(cm,2)}")
