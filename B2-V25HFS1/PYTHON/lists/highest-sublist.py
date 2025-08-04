# extract highest sublist from  a list and that should contain unique elements
l=list(map(int,input().split()))
f=False
for i in range(len(l),0,-1):
    for j in range(len(l)-i+1):
        x=l[j:j+i]
        if len(x)==len(set(x)):
            print(x)
            f=True
            break
    if f:
        break
