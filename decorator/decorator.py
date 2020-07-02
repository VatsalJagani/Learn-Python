from utils import timer

@timer
def add(a, b):
    return a+b

def sub(a, b):
    return a-b
sub = timer(sub)
# above line is same as adding @timer decorator

print(add(2,3))
print
print(sub(5,2))
print
print(str(add.__name__))   # It's name is not add !!!