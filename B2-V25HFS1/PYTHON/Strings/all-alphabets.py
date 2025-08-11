s=input()
d={}
for i in s:
    d[i]=ord(i)
for i in range(97,123):
    if i not in d.values():
        print("No")
        break
else:
    print("yes")