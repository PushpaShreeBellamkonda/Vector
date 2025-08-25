# count number of vowels,consonants,digits ,special symbols in a string

def count(s):
    vc=cc=dc=sc=0
    for i in s:
        if i.isdigit():
            dc+=1
        elif i in "aeiou":
            vc+=1
        elif i in "bcdfghjklmnpqrstvwxyz":
            cc+=1
        else:
            sc+=1
    return vc,cc,dc,sc
s=input()
print(count(s))

