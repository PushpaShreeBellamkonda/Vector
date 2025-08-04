n=int(input())
while n>0:
    ld=n%10
    if ld==5 or ld==7:
        print("target is found")
        break
    n=n//10
else:
    print("target not found")
