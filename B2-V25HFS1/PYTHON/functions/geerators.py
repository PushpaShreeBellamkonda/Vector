# display 1 to n numbers

def fun(n):
    for i in range(1,n+1):
        yield i   #if we use return it only gives 1st occurance
print(list(fun(5)))

# display  1st n terms in fibonacci sequence

def fun1(n):
    a=-1
    b=1
    for i in range(1,n+1):
        c=a+b
        yield c
        a,b=b,c
print(list(fun1(8)))