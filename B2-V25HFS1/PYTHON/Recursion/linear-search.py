def lsearch(l,k,i=0):
    if i==len(l):
        return -1
    elif l[i]==k:
        return i
    else:
        return lsearch(l,k,i+1)
l=list(map(int,input().split()))
k=int(input())
print(lsearch(l,k))