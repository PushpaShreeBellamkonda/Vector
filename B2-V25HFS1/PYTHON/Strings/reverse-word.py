# reverse every word in a sentance in place
s=input().split()
r=[]
for i in s:
    r.append(i[::-1])
print(" ".join(r))

# m-2

s1=input()
for i in s:
    s.replace(i[::-1] , i)
print(s)