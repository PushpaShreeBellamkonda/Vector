a=int(input())
b=int(input())
ch=input()
match ch:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '//':
        print(a//b)
    case '%':
        print(a%b)
    case '**':
        print(a**b)
    case _:
        print("enter valid operator")