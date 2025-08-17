n=int(input())
for i in range(n):
    s=input()
    s_r=s[::-1]
    l=[]
    l1=[]
    for i in s:
        l.append(ord(i))
    for i in s_r:
        l1.append(ord(i))
    for i in range(len(l)-1):
        if abs(l[i]-l[i+1]) != abs(l1[i]-l1[i+1]):
            print("Not Funny")
            break
    else:
        print("Funny")
        