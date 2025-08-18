s=input().lower()
d={}
for i in s:
    d[i]=ord(i)
for i in range(97,123):
    if i not in d.values():
        print("not pangram")
        break
else:
    print("pangram")