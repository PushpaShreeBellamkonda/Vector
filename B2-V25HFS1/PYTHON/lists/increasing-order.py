# check if given list is in increasing order

# m-1

l=list(map(int,input().split()))
if all(l[i]<l[i+1] for i in range(len(l)-1)):
    print("yes")
else:
    print("No")


# m-2

l=list(map(int,input().split()))
for i in range(1,len(l)):
    if l[i-1]>l[i]:
        print("No")
        break
else:
    print("yes")
