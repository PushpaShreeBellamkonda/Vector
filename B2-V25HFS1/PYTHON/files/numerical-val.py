f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/numbers.txt","r")
s=f.read()
print(s,type(s))
s1=[]
r=""
for i in s:
    if i.isdigit():
        r+=i
    else:
        if r: #if we finished a number
            s1.append(r)
            r=""
if r:  #r in end of the string
    s1.append(r)  
print(s1)
f.close()