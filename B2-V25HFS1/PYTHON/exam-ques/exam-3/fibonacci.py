# n terms in fibonacci sequence
def fib(n):
    a=-1
    b=1
    for i in range(n):
        c=a+b
        print(c)
        a,b=b,c
n=int(input())
print(fib(n))
    