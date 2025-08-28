# smallest among three numbers
def smallest(a,b,c):
    if a<b and a<c:
        return a
    elif b<c:
        return b
    else:
        return c
a,b,c=map(int,input().split())
print(smallest(a,b,c))