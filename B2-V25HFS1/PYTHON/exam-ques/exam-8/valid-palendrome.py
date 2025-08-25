# check if given string is a valid palendrome by ignoring spaces and case

def valpal(s):
    s=s.lower()
    s=s.replace(" ","")
    return s==s[::-1]
s=input()
print(valpal(s))
