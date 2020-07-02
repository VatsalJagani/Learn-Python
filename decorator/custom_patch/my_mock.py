class MyMockMagic(object):
    def __init__(self, func):
        self.func = func
        self.return_value = None
    
    def __call__(self, *args, **kwargs):
        if not self.return_value:
            self.func(*args, **kwargs)
        else:
            return self.return_value


def my_patch(target, return_value=None):
    def fn1(func):
        def fn2(*args, **kwargs):
            mock = MyMockMagic(target)
            if return_value:
                mock.return_value = return_value
            func(mock)
        return fn2
    return fn1