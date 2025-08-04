x1,v1,x2,v2=map(int,input().split())
if v1==v2:
    print("YES" if x1==x2 else "NO")
elif (x2-x1) % (v1-v2) ==0 and (v1-v2) *(x2-x1)>0:
    print("YES")
else:
    print("NO")