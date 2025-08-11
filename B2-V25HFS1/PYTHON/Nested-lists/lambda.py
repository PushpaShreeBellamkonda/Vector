n=int(input())
l=[]
for i in range(n):
    l.append([int(input()),input(),input(),float(input())]) #id,name,branch,marks
print(l)
# by default sort() or sorted() will sort based on 1st col
print(sorted(l,reverse=True))
# sort based on 1st col i.e name
print(sorted(l,key=lambda x:x[1]))
# soet based on branch wise,within branch marks wise
print(sorted(l,key=lambda x:(x[2],x[3])))
