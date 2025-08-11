# add elements in a list which are in different types

l=[3,6,3.4,[2,3,4],9 , [5,6,7]]
# l=eval(input())  --> can also be used
s=0
for i in l:
    if type(i)==list:
        s+=sum(i)
    else:
        s+=i
print(s)