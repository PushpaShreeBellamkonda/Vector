n=int(input())
l=[]
for _ in range(n):
    l.append(list(input()))
sets=[set(i) for i in l]
r=set.intersection(*sets)
print(len(r))