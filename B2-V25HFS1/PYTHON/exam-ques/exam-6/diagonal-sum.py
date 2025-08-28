# diagonal elements sum in a square matrix
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
ps=0 #principal diagonal sum
os=0 #absolute diagonal sum
for i in range(n):
    ps+=l[i][i]
    os+=l[i][n-i-1]
print(ps,os)