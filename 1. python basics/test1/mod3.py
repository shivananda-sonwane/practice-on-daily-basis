def f31(**kwargs):
    return [kwargs.keys() for i in kwargs]

def f32(**kwargs):
    return [kwargs.values() for i in kwargs]

def f33(**kwargs):
    return [kwargs.items() for i in kwargs]