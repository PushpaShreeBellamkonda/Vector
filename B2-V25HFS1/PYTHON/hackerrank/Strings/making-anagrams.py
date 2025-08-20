s1=list(input())
s2=list(input()) 
x=len(s1) 
y=len(s2) 
for i in s1: 
    if i in s2: 
        x-=1 
        y-=1
        s2.remove(i) 
print(x+y)