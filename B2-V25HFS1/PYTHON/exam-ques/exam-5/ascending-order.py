# list is in ascending order or not
def fun(l):
    for i in range(1,len(l)):
        if l[i]>l[i+1]:
            print("NO")
            break
    else:
        print("YES")
l=list(map(int,input().split()))
fun(l)