l=[5,4,4,2,2,1]
while l:
    print(len(l))
    m=min(l)
    l=[i-m for i in l if i-m>0]