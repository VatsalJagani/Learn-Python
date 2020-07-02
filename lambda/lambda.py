def add1(a, b):
    return a + b

add2 = lambda a, b: a + b

print(add1(1,3))
print
print(add2(1,3))
print

print(str(type(add1)))
print(str(add1.__name__))
print(str(type(add2)))
print(str(add2.__name__))
# name of lambda function is not the name of the function, it is "lambda"