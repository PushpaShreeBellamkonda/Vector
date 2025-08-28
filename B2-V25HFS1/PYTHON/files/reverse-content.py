# reverse the entire content of a file
f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/data.txt","r")
s=f.read()
f.close()
f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/reverse-content.txt","w")
f.write(s[::-1])
f.close()