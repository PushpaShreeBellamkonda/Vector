n=int(input())
if n % 3 == 0 and n % 5 == 0:
    print(n, "is divisible by both 3 and 5")
elif n%3==0:
    print(n,"is divisible by 3")
elif n%5==0:
    print(n,"is divisible by 5")
else:
    print("Not divisible by either 3 or 5")