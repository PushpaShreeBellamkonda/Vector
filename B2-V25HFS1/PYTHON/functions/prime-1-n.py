def isprime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
n=int(input())
for i in range(1,n+1):
    if isprime(i):
        print(i)