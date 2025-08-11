# m-1
s1=input()
s2=input()
if len(s1)==len(s2) and sorted(s1)==sorted(s2):
    print("yes")
else:
    print("No")

# m-2
s1=input()
s2=input()
if len(s1)==len(s2):
    for i in s1:
        s2=s2.replace(i,"",1)
    if len(s2)==0:
        print("yes")
    else:
        print("No")
else:
    print("No")