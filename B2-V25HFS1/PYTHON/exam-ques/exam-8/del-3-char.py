# delete every word 3rd character from a given string if len>5

def fun(s):
    if len(s)>5:
        s.remove(s[2])
        return "".join(s)
s=list(input())
print(fun(s))
    