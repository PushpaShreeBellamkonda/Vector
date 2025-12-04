r=int(input("enter rows"))
c=int(input("enter cols"))
l=[[int(input()) for m in range(c)] for n in range(r)]
print(l)
# col with max element
for i in range(r):
    max=l[0][i]
    for j in range(c):
        if l[j][i]>max:
            max=l[j][i]
    print(max)
# row with max element
max1=l[0][0]
for i in l:
    for j in i:
        if j>max1:
            max1=j
    print(max1)


