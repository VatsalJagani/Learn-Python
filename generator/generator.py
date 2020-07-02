# This is generator function
def my_database():
    print("initialize database connection")
    some_database_object = "I'm database connection"
    yield some_database_object
    print("destroy database connection")
    yield


generator = my_database()
# Nothing from function executed yet, until we go for next()
print("generator: " + str(generator))
print("type(generator): " + str(type(generator)))

print("")   

db_obj = generator.__next__()   # for python2 next()
# Run until first yield

print("hello do something with database!!!")
print(db_obj)

generator.__next__()
# Run until second yield
# If no yield found then StopIteration exception will come


# generator can also be used with foreach loop
print("")
print("generator with foreach loop")
for i in my_database():
    print(i)