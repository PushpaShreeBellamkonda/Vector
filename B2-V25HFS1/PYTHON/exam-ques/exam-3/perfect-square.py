# perfect squares b/w m to n
def perfect(m,n):
    for i in range(m,n+1):
        sqr=int(i**0.5)
        if sqr*sqr==i:
            print(i)
m=int(input())
n=int(input())
perfect(m,n)