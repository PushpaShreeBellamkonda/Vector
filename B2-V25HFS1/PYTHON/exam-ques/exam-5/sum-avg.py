# sum and avg of all elements 
def fun(l):
    sum=0
    for i in l:
        sum+=i
    return sum,(sum//len(l))
l=list(map(int,input().split()))
print(fun(l))