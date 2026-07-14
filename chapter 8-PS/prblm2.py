# celsius to fahrenheit

"c/5 = (f-32)/9"

def cel_to_fah(f):
    return (5*(f-32)/9)

f = int(input("Enter the fah value: "))
c = cel_to_fah(f)
print(round(c,2))