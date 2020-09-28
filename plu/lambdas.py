scientists = ['M C', 'A E', 'N B', 'I N', 'D M', 'A L', 'C L', 'A W', 'C D']
print(scientists)
print(sorted(scientists, key = lambda name: name.split()[-1]))

last_name = lambda name: name.split()[-1]

print(last_name("Nikolo Picolo"))