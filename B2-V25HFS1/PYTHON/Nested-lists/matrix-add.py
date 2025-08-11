r=int(input())
c=int(input())
a=[[int(input()) for j in range(c)] for i in range(r)]
b=[[int(input()) for j in range(c)] for i in range(r)]
c=[[a[i][j]+b[i][j] for j in range(c)] for i in range(r)]
print(c)