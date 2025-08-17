t=input()
if t[:2] =="12" and t[8:]=="PM":
    print(t[:8])
elif t[:2]=="12" and t[8:]=="AM":
    s=t[:2]
    s=int(s)-12
    print("{:02d}{}".format(int(s), t[2:8]))
elif t[8:] == "AM":
    print(t[:8])
else:
    s=t[:2]
    s=int(s)+12
    print("{:02d}{}".format(int(s), t[2:8]))
    