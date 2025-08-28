# minimum digit from a given number
def fun(n):
    min=9
    while n!=0:
        ld=n%10
        if ld<min:
            min=ld
        n=n//10
    return min
n=int(input())
print(fun(n))
