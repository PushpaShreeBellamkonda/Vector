# count how many characters ,words,lines available in a given file

f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/exam-ques/exam-10/data.txt","r")
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