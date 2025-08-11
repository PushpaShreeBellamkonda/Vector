s=input()
o=list(s)
r=[]
for i in range(len(o)):
    r.insert(i,o.pop())
if r==list(s):
    print("yes")
else:
    print("No")


# m-2
s=input()
i=0
j=len(s)-1
while i<j:
    if s[i]!=s[j]:
        print("No")
    else:
        i+=1
        j-=1
else:
    print("Yes")