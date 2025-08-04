n=int(input())
m = [list(map(int, input().split())) for _ in range(n)]
counts=[]
for a,b in m:
    c=0
    for i in range(a,b+1):
        sqr=int(i**0.5)
        if sqr*sqr==i:
            c+=1
    counts.append(c) 
# print(" ".join(str(i) for i in counts))          
for i in counts:
    print(i)

# m-2

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    t_sqr=0
    for i in range(1,b+1):
        sqr=i**2
        for j in range(a,b+1):
            if j==sqr:
                t_sqr+=1
    print(t_sqr)

            
        