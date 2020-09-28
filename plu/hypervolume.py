def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        for item in i:
            print(item)
            print(next(i))
            print(item)

        print(lengths)
        print("long",length)
        print("pre",v)
        v *= length
        print("vee",v)
    return v

print(hypervolume(2,3,4,5,6,7))