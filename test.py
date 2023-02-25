
class class_decorator:
    def __init__(self, fn):
        self.fn = fn

    def __set_name__(self, owner, name):
        # do something with owner, i.e.
        init_fn = owner.__init__
        def wrapper(self, *args, **kwargs):
            init_fn(self, *args, **kwargs)
            print(self.my_val)
        setattr(owner, "__init__", wrapper)



class MyClass():
    def __init__(self) -> None:
        self.my_val = 10

    @class_decorator
    def my_func(self):
        pass

MyClass()