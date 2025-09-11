try:
    n=int(input())
    if n<0:
        raise Exception("value should be greater than 0")
    else:
        print(n)
except Exception as e:
    print(e)