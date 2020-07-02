import time

def timer(funct):
    print("Decorator on: " + str(funct))   # This is memory pointer at function or class

    def function_with_timer_functionality(*args, **kwargs):
        current_time = time.time()
        print("Function " + str(funct.__name__) + " started")
        res = funct(*args, **kwargs)
        print("Execution time: " + str(time.time()-current_time))
        return res
    return function_with_timer_functionality


def patch(args):
    print("args to decorator: " + str(type(args)) + " : " + str(args))
    def decorator_with_parameters(funct):
        def anno(*args, **kwargs):
            # print("args: " + str(args))
            # print("kwargs: " + str(kwargs))
            res = funct(*args, **kwargs)
            return res
        return anno
    return decorator_with_parameters