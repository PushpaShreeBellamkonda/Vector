# col wise sum
r=int(input())
c=int(input())
l=[[int(input()) for j in range(c)] for i in range(r)]
print(l)
for j in range(c):
    s=0
    for i in range(r):
        s+=l[i][j]
    print(s)