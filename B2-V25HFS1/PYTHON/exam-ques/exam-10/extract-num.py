f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/exam-ques/exam-10/data.txt","r")
s=f.read()
for i in s:
    if i.isdigit():
        print(i)
        