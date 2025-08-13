s=input()
i=0
j=len(s)-1
m=0
while i<j:
    m=m+abs(ord(s[i])-ord(s[j]))
    j-=1
print(m)