## BASIC
dic = [i for i in range(10)]
print(dic)

settt = {i for i in range(10)}
print(settt)
g = (i for i in range(10))
print(g)
for item in g:
    print(item)

mult = [(x,y) for x in range(5) for y in range(3)]
print(mult)