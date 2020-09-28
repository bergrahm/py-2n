positives = filter(lambda x: x >0, [1,-1,1,10,-10])

for item in positives:
    print(item)

trues = filter(None, [0, None, 1, False, True, [], [1,2,3,], '', 'hello'])

for item in trues:
    print(item)

import operator
values = []