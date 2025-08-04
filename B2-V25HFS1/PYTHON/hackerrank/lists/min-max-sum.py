l=list(map(int,input().split()))
l.sort()
print(sum(l)-max(l),sum(l)-min(l))