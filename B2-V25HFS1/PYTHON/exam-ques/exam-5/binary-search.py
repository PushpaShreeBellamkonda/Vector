# binary search
def binary(l,k):
    lb=0
    ub=len(l)-1
    while lb<=ub:
        m=(lb+ub)//2
        if l[m]==k:
            return m
        elif k<l[m]:
            ub=m-1
        else:
            lb=m+1
    return -1
l=list(map(int,input().split()))
k=int(input())
print(binary(l,k))