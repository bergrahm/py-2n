g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g,p,l)
    inner()

outer()

def raise_to(exp):
    def raise_to_exp(x):
        return pow(x,exp)
    return raise_to_exp

square = raise_to(2)
print(square(3))
cube = raise_to(3)
print(cube(3))
hyper4 = raise_to(4)
print(hyper4(3))


# from closure import make_timer
# t = make_timer()
# t()
# t()
# t1() t2() would keep independent times. 
import time
def make_timer():
    last_called = None
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
        result = now - last_called
        last_called = now
        return result
    return elapsed