# if string contains all alphabets or not
# eg the quick brown fox jumps over the lazy dog
def alls(s):
    d={}
    for i in s:
        d[i]=ord(i)
    for i in range(97,124):
        if i in d.values():
            return True
    else:
        return False
s=input()
print(alls(s))
