# replace every el in a list with prod of all other ele
def prod(l):
    p=1
    for i in l:
        p=p*i
    for i in range(len(l)):
        l[i]=p//l[i]
    return l
l=list(map(int,input().split()))
print(prod(l))