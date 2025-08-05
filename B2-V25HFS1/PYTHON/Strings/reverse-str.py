s=input()
# print(s[::-1])
s=list(s)
for i in range(len(s)):
    s.insert(i,s.pop())
print("".join(s))

