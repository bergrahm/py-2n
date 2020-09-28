def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))


t = (12,13,14) +(10,10,10)
print(sum(t))

sun = [12,13,14,15,16]
mon = [13,14,15,16,17]

for item in zip(sun,mon):
    print(item)

from pprint import pprint as pp
daily = [sun, mon]
pp(daily)

five = 5

transposed = list(zip(*daily))
pp(transposed)