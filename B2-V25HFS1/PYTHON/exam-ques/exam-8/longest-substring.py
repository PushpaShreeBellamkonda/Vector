# find the longest substring without repeating character
def longest(s):
    for i in range(len(s),0,-1):
        for j in range(len(s)-i+1):
            t=s[j:j+i]
            if len(set(t))==len(t):
                return t
    return ""
s=input()
print(longest(s))