
n=int(input())
c=0
while n!=0:
    d=n%10
    c+=d
    n=n//10
print(c)

"""
sum of individual digits until the number become a single digit
"""

n=int(input())
while n>9:
    s=0
    while n!=0:
        s=s+n%10
        n=n//10
    n=s
print(n)
