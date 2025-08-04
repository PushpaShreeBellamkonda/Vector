# Find the index position whose left side values sum is equal to right side values sum ,
# if no such index , print -1

# m-1

l=list(map(int,input().split()))
ts=sum(l)
ls=0
for i in range(len(l)):
    rs=ts-ls-l[i]
    if rs==ls:
        print(i)
        break
    ls+=l[i]
else:
    print(-1)

# m-2

l=list(map(int,input().split()))
s=[0]
for i in range(len(l)):
    s.append(s[i]+l[i])
for i in range(len(l)):
    if s[i]==s[-1]-s[i+1]:
        print(i)
        break
else:
    print(-1)

# m-3 (using slicing)

l=list(map(int,input().split()))
for i in range(len(l)):
    if sum(l[:i])==sum(l[i+1:]):
        print(i)
        break
else:
    print(-1)
