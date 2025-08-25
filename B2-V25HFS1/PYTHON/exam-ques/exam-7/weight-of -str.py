# weight of string a=1,b=2..
def weight(s):
    w=0
    for i in s:
        w+=ord(i)-96
    return w
s=input()
print(weight(s))