# how many times each element occurs in a list
def fun(l):
    d={}
    for i in l:
        d[i]=d.get(i,0)+1
    return d
l=list(map(int,input().split()))
print(fun(l))