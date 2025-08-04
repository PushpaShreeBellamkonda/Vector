#for even

n=int(input())
for i in range(1,n+1):
    if i % 2 == 0 and i % 4!= 0:  #or if n%4==0:
        print(i)
print()
#for odd

n = int(input("Enter a number: "))
count = 0  
for i in range(1, n+1):
    if i % 2 == 1: 
        if count % 2 == 0: 
            print(i)
        count += 1


