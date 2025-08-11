# check if given string is palendrome or not without considering spaces,case(upper,lower)
s=input().lower()
s=s.replace(" ","")
if s==s[::-1]:
    print("yes")
else:
    print("No")