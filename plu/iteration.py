iterable = ['Spring', 'Summer', ' Autumn', 'Winter']
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Generator functions - these are iterators 
def gen123():
    yield 1,2,3
    yield 2


def gen246():
    print("yielding 2")
    yield 2
    print("yieldin 4")
    yield 4
    print("yielding 6")
    yield 6
    print("STOP")



g = gen123()
print(next(g))
print(next(g))

g = gen246()
print(next(g))
print(next(g))
print(next(g))

def lucas():
    yield 2
    a = 2
    b = 1
    while b < 10000:
        yield b
        a,b = b, a+b

for x in lucas():
    print(x)

# GENERATOR EXPRESSION
million_squares = (x*x for x in range(1, 1000001))
#print(million_squares)


print(sum(x*x for x in range(1, 4)))


# islice

from itertools import count, islice

#any(is_prime(x) for x in range(1328, 1361)) -> false


# zip
monday = [12, 12, 12, 12]
sunday = [14, 14, 14, 14]
tuesda = [15, 15, 15, 15]

for item in zip(monday, sunday):
    print(item)



for sun, mon in zip(sunday, monday):
    print("average =", (sun+mon)/2)

for temps in zip(monday, tuesda, sunday):
    print(f"min = {min(temps):4.1f}, max = {max(temps):4.1f}")