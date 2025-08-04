n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==(n+1)-i:
            print("*",end="")
        else:
            print("--",end="")
    for j in range(1,n):
        if j+1==i:
            print("-*",end="")
        else:
            print("--",end="")
    for j in range(1,n+1):
        if j==(n+1)-i and i!=n:
            print("*",end="")
        elif j==(n+1)-i and i==n:
            print("",end="")
        else:
            print("--",end="")
    for j in range(1,n):
        if j+1==i:
            print("-*",end="")
        else:
            print("--",end="")
    print()