import math
def sherlock(n):
    for _ in range(n):
        a,b=map(int,input().split())
        s=math.ceil(math.sqrt(a))
        e=math.floor(math.sqrt(b))
        c=e-s+1
        if c<0:
            c=0
        print(c)
n=int(input())
sherlock(n)

            
        