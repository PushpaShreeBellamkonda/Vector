n=int(input())
for _ in range(n):
    s=input()
    if len(s)%2!=0:
        print(-1)
    else:
        h=len(s)//2
        s1=list(s[:h])
        s2=list(s[h:])
        for i in s1[:]:
            if i in s2:
                s1.remove(i)
                s2.remove(i)
        print(max(len(s1),len(s2)))