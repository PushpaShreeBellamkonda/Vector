#prime or not

n=int(input())
if n<2:
    print("Not Prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("Prime") 


#  prime numbers from 1 to n

n=int(input())
for i in range(2,n+1):  
    for j in range(2,i): # we can also give (2,i//2+1)
            if i%j==0:
                break
    else:
        print(i,end=' ')

print()

#first n prime numbers

n=int(input())
c=0
i=2
while True:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        c=c+1
        print(i)
        if c==n:
            #print(i) for nth prime number
            break
    i+=1
