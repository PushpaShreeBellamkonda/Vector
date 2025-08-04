pmr=int(input("enter pmr:"))
cmr=int(input("enter cmr:"))
if pmr<cmr:
    nou=cmr-pmr
    if nou>=0 and nou<=100:
        print("current bill is :",nou*2.5)
    elif nou>=101 and nou<=150:
        print("current bill is :",nou*5.4)
    elif nou>=151 and nou<=200:
        print("current bill is :",nou*7.2)
    else:
        print("current bill is :",nou*9.8)
else:
    print("Error, previous meter should be less than current reading")
    
    
    
    