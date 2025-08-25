# super reduction on a string by iteratively removing adjacent duplicate characters until no more can be removed
def reduced(s):
    s=list(s)
    i=0
    while len(s)-1:
        if s[i]==s[i+1]:
            s.pop(i)
            s.pop(i)
            i=0
        else:
            i+=1
    return "".join(s)
s=input()
print(reduced(s))
