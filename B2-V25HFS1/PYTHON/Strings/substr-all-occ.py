s=input()
sub=input()
i=0
while True:
    i=s.find(sub,i)
    if i==-1:
        break
    else:
        print(i)
        i+=1
