# reverse every word in a string while preserving the word order
def rev(s):
    r=[]
    for i in s:
        r.append(i[::-1])
    return " ".join(r)
s=input().split()
print(rev(s))