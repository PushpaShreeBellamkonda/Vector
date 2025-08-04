n=int(input())
count=0
for i in range(1,n):
    if n%i==0:
        count+=i
if count==n:
    print("Perfect Number")
elif count < n:
    print("deficient Number")
else:
    print("Abundant Number")


