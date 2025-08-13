s=input()
s1=input()
i=0
for ch in s1:
    i=s.find(ch,i)
    if i==-1:
        print("No")
        break
    i+=1
else:
    print("Yes")