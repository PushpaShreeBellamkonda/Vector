s=input()
# print(s[::-1])
s=list(s)
for i in range(len(s)):
    s.insert(i,s.pop())
print("".join(s))
# m-2
s=input()
rev=" "
for i in s:
    rev=i+rev
print(rev)

# m-3

s=list(input())
i=0
j=len(s)-1
while i<j:
    s[i][j]=s[j][i]
    i+=1
    j-=1
print(" ".join(s))
