# elements divisible by 3 and 5
def div(l):
    for i in l:
        if i%3==0 and i%5==0:
            print(i)
l=list(map(int,input().split()))
div(l)