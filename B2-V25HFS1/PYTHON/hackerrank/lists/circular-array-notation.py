n,k,q=map(int,input().split())
l=list(map(int,input().split()))
queries=[int(input()) for _ in range(q)]
for i in range(k):
    l.insert(0,l.pop())
for query in queries:
    print(l[query])
    