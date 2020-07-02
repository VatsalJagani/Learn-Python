class MyClass:
    def __init__(self, some_fun):
        def fn():
            print("Hello World !!!")
        # set attr can set attribute to any class
        # here below line setting function as name of argument passed
        setattr(self, some_fun, fn)