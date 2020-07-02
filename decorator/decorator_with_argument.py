# Notice this is function within function within function
def decorator_with_parameters(args):
    # Of cource we can use *args, **kwargs here
    print("args to decorator: " + str(type(args)) + " : " + str(args))

    def decorator_with_parameters(funct):
        def anno(*args, **kwargs):
            # print("args: " + str(args))
            # print("kwargs: " + str(kwargs))
            print("Inside anno function")
            res = funct(*args, **kwargs)
            return res
        return anno
    return decorator_with_parameters


@decorator_with_parameters("The error message is this.")
def my_func(*args, **kwargs):
    print(str(args))
    print(str(kwargs))
    print("inside my_func")

print(my_func.__name__)
# it is anno
# It is always the most inner function

my_func("hello")