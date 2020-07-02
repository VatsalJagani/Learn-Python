
# Sonthing similar to 
# from contextlib import contextmanager
class MyContextManger(object):
    def __init__(self, func):
        self.func = func
        self.gen = func()
        # return self.func()

    def __enter__(self):
        # This should return when with is executed
        print("__enter__")
        return self.gen.__next__()

    def __exit__(self, *args, **kwargs):
        print("__exit__")
        self.gen.__next__()

    def __call__(self):
        # when my_database() is called this contextManager should return
        print("__call__")
        return self


@MyContextManger
def my_database():
    print("initialize database connection")
    some_database_object = "I'm database connection"
    yield some_database_object
    print("destroy database connection")
    yield


with my_database() as d:
    print(d)
    print("hello do something with database!!!")