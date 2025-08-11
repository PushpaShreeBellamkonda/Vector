s=input()
l=[]
for ch in s:
    if ch.isdigit():
        l.append(ch)
if len(l)>0:
    l.sort(reverse=True)
    for i in range(len(l)-1,-1,-1):
        if int(l[i])%2==0:
            l.append(l.pop(i))
            print(" ".join(l))
            break
    else:
        print(-1)
else:
    print(-1)