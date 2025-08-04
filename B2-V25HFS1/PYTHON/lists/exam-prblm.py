# Replace every element in a list with the product of all other elements 

l=list(map(int,input().split()))
p=1
for i in l:
    p=p*i
for i in range(len(l)):
    l[i]=p//l[i]
print(l)