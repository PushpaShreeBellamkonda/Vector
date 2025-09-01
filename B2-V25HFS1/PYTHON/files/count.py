# count how many characters ,words,lines available in a given file

# m-1
# f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/data.txt","r")
# s=f.read()
# l=s.count("\n")+1
# w=s.count(" ")+1
# c=len(s)-(l-1)
# print(l,w,c)
# f.close()

# m-2
f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/data.txt","r")
s=f.read()
c=0
l=w=1
for i in s:
    if i==" ":
        w+=1
        c+=1
    elif i=="\n":
        w+=1
        l+=1
    else:
        c+=1
print(l,w,c)
f.close()