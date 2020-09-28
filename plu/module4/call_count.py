class CallCount:
    def __init__(self, f):
        self.f = f
        self._count = 0
    
    def __call__(self, *args, **kwargs):
        self._count += 1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print("Hello, {}".format(name))
    print(hello._count)