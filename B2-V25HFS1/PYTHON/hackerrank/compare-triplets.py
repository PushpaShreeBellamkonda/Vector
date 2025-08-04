l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in range(l1):
    if l1[i]>l2[i]:
        l1c+=1
    elif l2[i]>l1[i]:
        l2c+=1
print(l1c,l2c)





