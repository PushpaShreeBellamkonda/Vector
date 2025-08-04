#first max digit

n=int(input())
max=0
while n!=0:
    d=n%10
    n=n//10
    if d>max:
        max=d
print(max)

#min digit

n=int(input())
min=9
while n!=0:
    d=n%10
    n=n//10
    if d<min:
        max=d
print(max)



