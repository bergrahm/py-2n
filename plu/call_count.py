class Call_Count:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count +=1 
        return self.f(*args, **kwargs)


@Call_Count
def ello(name):
    print('Hello {}'.format(name))

ello("sven")
ello("justin")
print(ello.count)