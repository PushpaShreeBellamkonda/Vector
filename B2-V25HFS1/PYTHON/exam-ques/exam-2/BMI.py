# bmi=weight(kg)/(height(m))^2
def bmi(w,h):
    bmi=w//(h**2)
    if bmi<18.5:
        print("Under weight")
    elif bmi>=18.5 and bmi<=24.9:
        print("Normal weight")
    elif bmi>=25 and bmi<=29.9:
        print("Over weight")
    elif bmi>=30:
        print("Obesity")
w=int(input())
h=int(input())
bmi(w,h)