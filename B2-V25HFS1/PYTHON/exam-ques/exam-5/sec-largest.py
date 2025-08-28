# display second largest element in a list
def sec(l):
    m=max(l)
    l.remove(m)
    return max(l)
l=list(map(int,input().split()))
print(sec(l))