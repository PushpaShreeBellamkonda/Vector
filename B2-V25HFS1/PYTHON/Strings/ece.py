s=input()
t=input()
l=[]
for ch in set(t):
    l.append(s.count(ch)//t.count(ch))
print(min(l))