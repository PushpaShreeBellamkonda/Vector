def decfun(fun):
    def updfun(n):
        return n*fun(n)
    return updfun
@decfun
def sqr(n):
    return n*n
print(sqr(5))

# update x+y functionality to (x+y)^2

def decfun(fun):
    def updfun(x,y):
        return fun(x,y)**2
    return updfun
@decfun
def add(x,y):
    return x+y
print(add(2,5))