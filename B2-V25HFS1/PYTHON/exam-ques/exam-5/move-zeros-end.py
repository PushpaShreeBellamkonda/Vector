# move all zeroes to end without changing nonzero elements position
def move(l):
    z=l.count(0)
    while 0 in l:
        l.remove(0)
    for i in range(z):
        l.append(0)
    return l
l=list(map(int,input().split()))
print(move(l))
        