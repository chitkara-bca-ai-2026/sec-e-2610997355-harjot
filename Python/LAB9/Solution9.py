#STAR TRIANGLE
n=int(input())
for rows in range(1,n+1):
    for columns in range(1,rows+1):
        print("*",end=" ")
    print()

#NUMBER TRIANGLE
n=int(input())
for rows in range(1,n+1):
    for columns in range(1,rows+1):
        print(columns,end=" ")
    print()

# INVERTED STAR TRIANGLE
n=int(input())
for rows in range(n,0,-1):
    for columns in range(1,rows+1):
        print("*",end=" ")
    print()

#ALPHABET TRIANGLE
n=int(input())
X="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for rows in range(1,n+1):
    for columns in range(1,rows+1):
        print(X[columns-1],end=" ")
    print()

#PYRAMID
'''outer loop(rows) control number of rows
first inner loop(columns) control number of star in each row
second loop (space) controls spaces in each row'''
for rows in range(1,n+1):
    for space in range(1,n-rows+1):
        print(" ",end="")
    for columns in range(1,2*rows):
        print("*",end="")
    print()