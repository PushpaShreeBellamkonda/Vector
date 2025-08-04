n=int(input())
a=5
b=8
c=9
for i in range(n-3):
    d=c+b-a
    a,b,c=b,c,d
print(d)