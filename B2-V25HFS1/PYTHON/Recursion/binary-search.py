def bsearch(arr,k,l,u):
    if l<u:
        m=(l+u)//2
        if arr[m]==k:
            return m
        elif k<arr[m]:
            return bsearch(arr,k,l,m-1)
        else:
            return bsearch(arr,k,m+1,u)
    else:
        return -1
l=list(map(int,input().split()))
k=int(input())
print(bsearch(l,k,0,len(l)-1))