# prime or not
def prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
n=int(input())
print(prime(n))