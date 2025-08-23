def isprime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
n=int(input())
i=1
c=0
while True:
    if isprime(i):
        print(i)
        c+=1
        if c==n:
            break
    i=i+1
