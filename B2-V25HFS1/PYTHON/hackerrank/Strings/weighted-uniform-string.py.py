s=list(input())
n=int(input())
queries=[int(input()) for _ in range(n)]
l=set()
prev=""
w=0
for i in s:
    val=ord(i)-96
    if i==prev:
        w+=val
    else:
        w=val
        prev=i
    l.add(w)
    
for i in queries:
    print("Yes" if i in l else "No")
    