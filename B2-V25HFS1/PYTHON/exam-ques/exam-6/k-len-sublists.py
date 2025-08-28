# k length subslist that contain non-duplicate elements
k=int(input())
l=list(map(int,input().split()))
print(l)
for i in range(len(l)-k+1):
    t=l[i:i+k]
    if k==len(set(t)):
        print(t)
        break
else:
    print(-1)
