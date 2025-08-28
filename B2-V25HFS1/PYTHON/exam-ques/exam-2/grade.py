def grade(m):
    if m>=90 and m<=100:
        print("EX")
    elif m>=70 and m<=89:
        print("Good")
    elif m>=50 and m<=69:
        print("Avg")
    elif m>=30 and m<=49:
        print("Poor")
    else:
        print("Fail")
m=int(input())
grade(m)