words = "Why sometimes I have believed as many as six impossible things before breafkast".split()
# Syntax
# expr(item) for item in iterable
print([len(word) for word in words])


# Dict comprehension
country_to_capital = {  'UK': 'London',
                        'Morocco':'Rabat',
                        'Sweden': 'Stockholm',}

capital_to_country = {capital: country for country, capital in country_to_capital.items()}

from pprint import pprint as pp
pp(capital_to_country)

# filtering comprehensions
from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) +1):
        if(x % i == 0):
            return False
    return True

print([x for x in range(42) if is_prime(x)], "\n", 10*"*")


prime_square_divisors = {x*x : (1, x , x*x) for x in range(42) if is_prime(x)}
print(prime_square_divisors)

numbas = (x*x for x in [1,2,3,4,5])
print(type(numbas))
for num in numbas:
    print(num)