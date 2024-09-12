# WRITE A PYTHON PROGRAM TO PRINT PATTERN -

n=5
for i in range(1,n+1):
    for j in range(0,i):
        if(j==0 or j==i-1):
            print(chr(65+j),end="")
        else:
            print(" ",end="")
    for j in range(0,2*(n-i)):
        print(" ",end="")
    for j in range (0,i):
        if(j==0 or j==i-1):
            print(chr(65+j),end="")
        else:
            print(" ",end="")
    print()
for i in range(1,n+1):
    k=0
    for j in range(n,i-1,-1):
        if(j==n or j==i):
            print(chr(65+k),end="")
        else:
            print(" ",end="")
            k=k+1
    for j in range(1,2*i-1):
        print(" ",end="")
    k=0
    for j in range(n,i-1,-1):
        if(j==n or j==i):
            print(chr(65+k),end="")
        else:
            print(" ",end="")
        k=k+1
    print()