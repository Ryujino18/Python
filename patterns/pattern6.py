"""
    *
   **
  ***
 ****
*****

"""
n = 5

for i in range(1, n + 1):

    # Spaces
    for j in range(1, n - i + 1):
        print(" ", end="")

    # Stars
    for k in range(1, i + 1):
        print("*", end="")

    print()