# common elements b/w two lists
def common(l1,l2):
    for i in l1:
        if i in l2:
            print(i)
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
common(l1,l2)