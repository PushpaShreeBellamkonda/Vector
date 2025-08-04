n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    count=0
    for i in c:
        if i<=0:
            count+=1
    if count>=b:
        print("NO")
    else:
        print("YES")
            