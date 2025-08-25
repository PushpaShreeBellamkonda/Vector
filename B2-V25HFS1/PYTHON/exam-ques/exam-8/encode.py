# encode a string "aaabbcdaa"->a3b2c1d1a2

def encode(s):
    en=""
    c=0
    a=s[0]
    for i in s:
        if i==a:
            c+=1
        else:
            en+=a+str(c)
            c=1
            a=i
    en+=a+str(c)
    return en
s=list(input())
print(encode(s))
