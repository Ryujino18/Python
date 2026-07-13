"""

*****
*   *
*   *
*****


"""


# n = 4
# for i in range(1,n-1):
#     print("*",end='') #first
#     for i in range (i,n-2):
#         if(i==1 or i ==n):
#             print("*")
#         else:
#             print("")

#     print("*", end='')#last

n = 4      # rows
m = 5      # columns

for i in range(1, n + 1):
    for j in range(1, m + 1):

        if i == 1 or i == n:      # First and last row
            print("*", end="")
        else:                     # Middle rows
            if j == 1 or j == m:
                print("*", end="")
            else:
                print(" ", end="")

    print()