# reverse line by line content in a file
f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/data.txt","r")
l=f.readlines()
print(l)
f.close()
l[0]=l[0].strip()
l[-1]=l[-1]+"\n"
print(l)
for i in range(len(l)):
    l[i]=l[i][::-1]
print(l)
f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/reverse-line.txt","w")
f.writelines(l)
f.close()