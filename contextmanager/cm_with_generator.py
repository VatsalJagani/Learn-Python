from contextlib import contextmanager

@contextmanager
def my_database():
    print("initialize database connection")
    some_database_object = "I'm database connection"
    yield some_database_object
    print("destroy database connection")


with my_database() as d:
    print(d)
    print("hello do something with database!!!")