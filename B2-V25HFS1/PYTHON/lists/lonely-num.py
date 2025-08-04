#  In a list except one number , remaining all the numbers are repeated morethan once, display the lonely number

l=list(map(int,input().split()))
for i in set(l):
    if l.count(i)==1:
        print(i)
        break