def fn(**kwargs):
    '''
    *kwargs is used to pass variable number of arguments to a function
    *kwargs only accepts argument with keyword
    *kwargs is a dict
    *kwargs is also accept zero arguments
    '''
    print("type of kwargs: " +str(type(kwargs)))
    print("kwargs: " + str(kwargs))
    for i in kwargs.items():
        print(str(i))


fn(a=[25, 10], b="Hello", c={40})

fn()