n=int(input())
for _ in range(n):
    s=list(input())
    s1=[]
    s2=[]
    if len(s)%2==0:
        for i in range(len(s)//2):
            s1.append(s[i])
        for i in range(i+1,len(s)):
            s2.append(s[i])
    else:
        print(-1)
    c=0
    for i in s1:
        if i in s2:
            c+=1
    print(len(s1)-c)
            
        