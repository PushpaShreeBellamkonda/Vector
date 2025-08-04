# sublist finding
l=list(map(int,input().split()))
for i in range(len(l),0,-1):
    for j in range(len(l)-i+1):
        print(l[j:j+i] , end="\n")



# k length sublist
l=list(map(int,input().split()))
i=int(input())
for j in range(len(l)-i+1):
    print(l[j:j+i])