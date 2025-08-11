s=input().split()
m=1
w=s[0]
for i in s:
    if len(i)>m:
        m=len(i)
        w=i
print(w)

# m-2
s=input().split()
s.sort(reverse=True,key=lambda x:len(x))
print(s[0])
# to print all max len words
for i in range(len(s-1)):
    if len(i)==len(i+1):
        print(i+1)
    else:
        break
