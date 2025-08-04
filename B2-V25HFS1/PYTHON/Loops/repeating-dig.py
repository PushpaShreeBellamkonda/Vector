n=int(input())
target=int(input())
count=0
while n>0:
    ld=n%10
    if ld==target:
        count+=1
    n=n//10
print(f"count of {target} is {count}")
