a=list(map(int,input().split()))
k=int(input())
lb=0
ub=len(a)-1
while lb < ub:
    mid=(lb+ub)//2
    if a[mid]==k:
        print(mid)
        break
    elif k < a[mid]:
        up=mid-1
    else:
        lb=mid+1
else:
    print(-1)
