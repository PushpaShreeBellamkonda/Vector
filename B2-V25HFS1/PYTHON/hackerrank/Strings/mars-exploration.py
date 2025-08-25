def mars(s):
    c=0
    s1="SOS"
    for i in range(len(s)):
        if s[i]!=s1[i%3]:
            c+=1
    return c
s=input()
print(mars(s))