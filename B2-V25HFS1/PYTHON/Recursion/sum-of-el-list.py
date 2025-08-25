def sum(l,i=0):
    if i==len(l)-1:
        return l[i]
    else:
        return l[i]+sum(l,i+1)
l=list(map(int,input().split()))
print(sum(l))