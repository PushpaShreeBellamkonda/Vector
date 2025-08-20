n=int(input())
for _ in range(n):
    s=input()
    i=0
    j=len(s)-1
    m=0
    while i<j:
        m+=abs((ord(s[i])-ord(s[j])))
        i+=1
        j-=1
    print(m)
