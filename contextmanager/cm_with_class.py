# For some class to be an ContextManager __enter__ and __exit__ is required.

class MyDatabase(object):
    def __init__(self):
        pass
    def __enter__(self):
        print("initializing database connection")
        return "I'm database connection"
    def __exit__(self, *args, **kwargs):
        print("destroying database connection")

with MyDatabase() as d:
    print(d)
    print("hello do something with database!!!")