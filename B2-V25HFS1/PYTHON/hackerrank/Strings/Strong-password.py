n1=int(input())
p=input()
n= "0123456789"
l = "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s= "!@#$%^&*()-+"
c=0
if not any(i in n for i in p):
    c+=1
if not any(i in l for i in p):
    c+=1
if not any(i in u for i in p):
    c+=1
if not any(i in s for i in p):
    c+=1   
print(max(c,6-len(p)))