def leap(y):
    if (y%400==0) or (y%4==0 and y%100!=0):
        return True
def leap1(y):
    if (y%4==0):
        return True
y=int(input())
if y==1918:
    print("26.09.1918")
elif y<=1917:
    if leap1(y):
        print(f"12.09.{y}")
    else:
        print(f"13.09.{y}")
else:
    if leap(y):
        print(f"12.09.{y}")
    else:
        print(f"13.09.{y}")


    