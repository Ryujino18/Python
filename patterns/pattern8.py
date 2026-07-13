"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

"""

n = 5

# Upper Pyramid
for i in range(1, n + 1):

    # Spaces
    for j in range(1, n - i + 1):
        print(" ", end="")

    # Stars
    for k in range(1, 2 * i):
        print("*", end="")

    print()

# Lower Pyramid
for i in range(1, n):

    # Spaces
    for j in range(1, i + 1):
        print(" ", end="")

    # Stars
    for k in range(1, 2 * (n - i)):
        print("*", end="")

    print()

    