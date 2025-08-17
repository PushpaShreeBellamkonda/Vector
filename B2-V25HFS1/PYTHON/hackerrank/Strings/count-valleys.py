n=int(input())
p=input()
c=c1=0
for i in p:
    prev=c
    if i=="U":
        c+=1
    elif i=="D":
        c-=1
    if c==0 and prev < 0:
        c1+=1
print(c1)