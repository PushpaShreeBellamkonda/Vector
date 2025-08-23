def isprime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
def ispal(n):
    n=str(n)
    return n==n[::-1]
n=int(input())
while True:
    if isprime(n) and ispal(n):
        print(n)
        break
    else:
        n=n+1