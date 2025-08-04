# perfect or not

n=int(input())
sqr=int(n**0.5)
if sqr*sqr==n:
    print("Perfect Square")
else:
    print("Not Perfect Square")

print()

# from 1 to n
n=int(input())
for i in range(1,n+1):
    sqr=int(i**0.5)
    if sqr*sqr==i:
        print(i)

print()

#from m to n

m=int(input())
l=int(input())
for i in range(m,l+1):
    sqr=int(i**0.5)
    if sqr*sqr==i:
        print(i)

print()

#to get count of perfect squares from m to n
m=int(input())
n=int(input())
print(int(n**0.5)-int((m-1)**0.5))
    