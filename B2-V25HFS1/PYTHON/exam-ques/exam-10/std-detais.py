# file contains all student details like id,name,dept,marks.Display all cse department student details
f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/exam-ques/exam-10/std-details.txt","r")
s=f.readlines()
for i in s:
    cols=i.strip().split(" ")
    if cols[2]=="cse":
        print(i)
f.close()