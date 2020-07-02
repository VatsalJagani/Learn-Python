def singleton(class_):
    print("class_: " + str(class_))
    instances = {}
    def fun(*args, **kwargs):
        if class_ in instances:
            return instances[class_]
        else:
            instances[class_] = class_(*args, **kwargs)
            return instances[class_]
    return fun


@singleton
class MyClass(object):
    def __init__(self, a):
        self.a = a


m = MyClass(1)
print(m.a)

m2 = MyClass(2)
print(m2.a)
# The value is still 1