# sum of individual digits of a number
def fun(n):
    s=0
    while n!=0:
        ld=n%10
        s+=ld
        n=n//10
    return s
n=int(input())
print(fun(n))
