# rotate list to left by k positons
def rotate(l,k):
    k=k%len(l)
    for i in range(k):
        l.append(l.pop(0))
        # l.append(0,l.pop()) rotate right
    return l
l=list(map(int,input().split()))
k=int(input())
print(rotate(l,k))
                    