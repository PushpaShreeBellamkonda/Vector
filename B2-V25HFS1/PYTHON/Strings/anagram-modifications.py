s1=input()
s2=input()
for ch in s1:
    if ch in s2:
        s1.replace(ch," ",1)
        s2.replace(ch," ",1)
print(max(len(s1),len(s2)))