#Given a number n, check if it is divisible by any number from 2 to n-1.
#  Use for-else to print whether it's divisible or not.

n=int(input())
for i in range(2,n-1):
    if n%i==0:
        print(i)
        break
else:
    print("Not divisible")