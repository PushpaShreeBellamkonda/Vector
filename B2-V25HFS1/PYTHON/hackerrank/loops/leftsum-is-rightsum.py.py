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





