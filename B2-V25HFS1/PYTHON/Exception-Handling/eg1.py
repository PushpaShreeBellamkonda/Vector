try:
    a=int(input())
    b=int(input())
    c=a/b
    # print(x)
except ValueError as v:
    print("Provide only integers")
except ZeroDivisionError as z:
    print("b value shouldnt be 0")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("end of program")
