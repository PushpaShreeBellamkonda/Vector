n=int(input())
for i in range(1,n+1):
    print("--"*(n-i),end="-")
    for j in range(1,i+1):
        print("*" if j==1 else "--",end="")
    for j in range(i-1,0,-1):
        print("-*" if j==1 else "--",end="")
    print("--"*(n-i),end="")
    print("-"*(2*(n-i)-2),end="-")
    for j in range(1,i+1):
        if j==1 and i!=n:
            print("*",end="")
        elif i==n and j!=1:
            print("-",end="")
        else:
            print("--",end="")
        # print("*" if j==1 and i!=n else "--",end="")
    for j in range(i-1,0,-1):
        if j==1 and i!=n:
            print("-*",end="")
        elif i==n and j==1:
            print("--*",end="")
        elif i==n and j==1:
            print("-",end="-")
        else:
            print("--",end="")
        # print("-*" if j==1 else "--",end="")
    print()
for i in range(n-1,0,-1):
    print("--"*(n-i),end="-")
    for j in range(1,i+1):
        print("*" if j==1 else "--",end="")
    for j in range(i-1,0,-1):
        print("-*" if j==1 else "--",end="")
    print("--"*(n-i),end="")
    print("-"*(2*(n-i)-2),end="-")
    for j in range(1,i+1):
        if j==1 and i!=n:
            print("*",end="")
        elif i==n and j!=1:
            print("-",end="")
        else:
            print("--",end="")
        # print("*" if j==1 and i!=n else "--",end="")
    for j in range(i-1,0,-1):
        if j==1 and i!=n:
            print("-*",end="")
        elif i==n and j==1:
            print("--*",end="")
        elif i==n and j==1:
            print("-",end="-")
        else:
            print("--",end="")
        # print("-*" if j==1 else "--",end="")
    print()

    
    
    


