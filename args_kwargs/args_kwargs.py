def fn(*args, **kwargs):
    '''
    A function that can accepts any type and any number of arguments
    '''
    for i in args:
        print(str(i))
    
    for i in kwargs.items():
        print(str(i))


fn([25, 10], a="Hello", b={40})

fn()
