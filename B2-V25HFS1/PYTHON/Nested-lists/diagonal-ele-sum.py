r=int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
print(l)
ps=0  #principal diagnal sum
os=0  #absolute diagonal sum
for i in range(r):
    ps+=l[i][i]
    os+=l[i][r-i-1]
print(ps)
print(os)