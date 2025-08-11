# reverse string without changing special symbol position
s=list(input())
i=0
j=len(s)-1
while i<j:
    if not s[i].isalnum():
        i+=1
    elif not s[j].isalnum():
        j-=1

    else:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
print("".join(s))