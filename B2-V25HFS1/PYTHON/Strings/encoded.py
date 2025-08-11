# from the given encoded string (a3b2k1s2e4a2)
# 1) display which character repeated highest times
# 2) display nth character in the original string

# 1
s=input()
d={}
for i in range(0,len(s),2):
    d[s[i]]=d.get(s[i],0)+int(s[i+1])
print(sorted(d.items(),key=lambda x:x[1],reverse=True)[0])
print(d)

# 2
s=input()
n=int(input())
c=0
for i in range(1,len(s),2):
    c+=int(s[i])
    if c>=n:
        print(s[i-1])
        break