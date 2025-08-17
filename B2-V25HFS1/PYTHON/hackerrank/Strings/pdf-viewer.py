h=list(map(int,input().split()))
s=input()
l=[]
for i in s:
    val=ord(i)-ord("a")
    l.append(int(h[val]))
print(max(l)*len(l))