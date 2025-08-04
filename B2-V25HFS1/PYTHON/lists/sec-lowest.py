# second highest

l=list(map(int,input().split()))
m=max(l)
while m in l:
    l.remove(m)
print(max(l))

# second lowest

l=list(map(int,input().split()))
m=min(l)
while m in l:
    l.remove(m)
print(min(l))


