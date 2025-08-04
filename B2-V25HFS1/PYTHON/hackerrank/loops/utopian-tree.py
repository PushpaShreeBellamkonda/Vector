x=int(input())
for _ in range(x):
    n=int(input())
    h=1
    if n>=1:
        for i in range(n):
            if i%2==0:
                h+=h
            elif i%2==1:
                h+=1
    print(h)