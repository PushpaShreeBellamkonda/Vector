# rotate k elements from left to right

l=list(map(int,input().split()))
k=int(input())
k=k%len(l)
for i in range(k):
    l.append(l.pop(0))
print(l)