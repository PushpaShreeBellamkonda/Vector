def ispal(n):
    n=str(n)
    return n==n[::-1]
n=int(input())
print(ispal(n))