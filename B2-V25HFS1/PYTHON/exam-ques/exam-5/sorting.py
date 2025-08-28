# insertion sort
def insertion(l):
    for i in range(1,len(l)):
        j=i-1
        while j!=-1 and l[j]>l[i]:
            j=j-1
        l.insert(j+1,l.pop(i))
    return l
l=list(map(int,input().split()))
print(insertion(l))