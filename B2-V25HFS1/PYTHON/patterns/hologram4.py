m=int(input())
n=int(input())
for i in range(1,m+1):
    for j in range(1,n+1):
        if j==1 or j==(n-i+1) or j==n or j==i :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
