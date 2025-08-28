# split a list into 2 lists ,one with even and one with odd numbers
def split(l):
    l1=[]
    l2=[]
    for i in l:
        if i%2==0:
            l1.append(i)
        elif i%2==1:
            l2.append(i)
    return l1,l2
l=list(map(int,input().split()))
print(split(l))