class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print("calling {}".format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

lust = [1,2,3,4,5,6]
print(lust)
lust = rotate_list(lust)
print(lust)
lust = rotate_list(lust)
print(lust)
lust = rotate_list(lust)
print("DISABUOLS")
tracer.enabled = False
print(lust)
lust = rotate_list(lust)
print("EN ABLee")
tracer.enabled = True
print(lust)
lust = rotate_list(lust)