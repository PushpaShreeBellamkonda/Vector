# display nuumbers div by 3 or 5 b/w 1-n
def fun(n):
    for i in range(1,n+1):
        if i%3==0 or i%5==0:
            print(i)
n=int(input())
fun(n)