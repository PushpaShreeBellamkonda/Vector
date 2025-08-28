# flatten a nested list 
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l1=[]
for i in l:
    for j in i:
        l1.append(j)
print(l1)