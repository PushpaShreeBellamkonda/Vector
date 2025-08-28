# calculate tax based on income
def tax(i):
    if i<1000000:
        return i*0.05
    elif i>=1000000 and i<=5000000:
        return i*0.15
    elif i>=5000000:
        return i*0.25
i=int(input())
print(tax(i))
    