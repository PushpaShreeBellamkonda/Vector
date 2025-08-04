n=int(input())
for _ in range(n):
    n,c,m=map(int,input().split())
    e=n//c
    w=e
    while w>=m:
        ne=w//m
        e+=ne
        w=ne+(w%m)
    print(e)