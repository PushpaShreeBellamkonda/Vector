s=input()
for i in range(len(s),1,-1):
    for j in range(len(s)-i+1):
        t=s[j:j+i]
        if t==t[::-1]:
            print(t)

