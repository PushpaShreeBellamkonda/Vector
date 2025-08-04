
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)

print()

n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count)

#using while

m=int(input())
count=0
j=1
while j<=n:
    if n%j==0:
        count+=1
    j+=1
print(count)