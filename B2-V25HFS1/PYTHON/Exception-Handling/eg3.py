class AE(Exception):
    def __init__(s,msg="invalid msg"):
        s.msg=msg
    def __str__(s):
        return s.msg
try:
    age=int(input())
    if age<=0 or age>100:
        raise AE("age need to be bw 1 to 100")
    else:
        print(age)
except AE as e:
    print(e)
    