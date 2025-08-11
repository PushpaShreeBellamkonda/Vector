# frequency count of each element in a list
l=list(map(int,input().split()))
d={}
for i in l:
    d[i]=d.get(i,0)+1
print(d)

# m-2
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
