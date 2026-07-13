'''

*****
*   *
*   *
*   *
*****

'''
n = 5
m=5

for i in range(1,n+1):
    for j in range(1,m+1):
        if (i == 1 or i ==n):
            print("*", end="")

        else:
            if(j==1 or j==m):
                print("*", end="")
            else:
                print(" ",end ="")
    print()

    