n=int(input())
l=[]
for _ in range(n):
    l.append(input())
s=sorted(l,key=lambda x:(len(x),x))
for i in s:
    print(i)