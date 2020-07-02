def fn(*args):
    '''
    *args is used to pass variable number of arguments to a function
    *args only accepts non-keyword arguments
    *args is a tuple
    *args is also accept zero arguments
    '''
#     print("type of *args " + str(type(*args)))
#     print("*args: " + str(*args))
#     print
    print("type of args: " + str(type(args)))
    print("args: " + str(args))
    for i in args:
        print(str(i))


fn([25, 10], "Hello", {40})

fn()

# fn(a="Hello World")