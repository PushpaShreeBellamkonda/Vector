l=list(map(int,input().split()))
k=int(input())
for i in range(len(l)):
    if k==l[i]:
        print("k founf at index: ",i)
        break
else:
    print("k not found")