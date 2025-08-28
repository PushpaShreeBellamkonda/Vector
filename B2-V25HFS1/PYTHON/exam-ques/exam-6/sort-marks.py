# read n students details and sort based on marks
n=int(input())
l=[]
for i in range(n):
    l.append([int(input()),input(),input(),float(input())])
    # id,name,branch,marks
print(l)
print(sorted(l,key=lambda x:x[3]))