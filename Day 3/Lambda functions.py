#lambda functions- small ananmous function (dont need def)
#can take multiple arguments
#often used for short and simple operations, especiually passing an function as an argument to other functions

#side-by-side
"""""
#regular functions
def sum(a, b):
    return a + b

print(sum(2, 3))


#lambda equiilant
sum_lambda = lambda a, b: a + b
print(sum_lambda(2, 3)) 
import math

def circle_perimeter(radius):
    return 2 * math.pi * radius

sum_lambda = lambda c, p, r: 2 * 3.14 * r

print(sum([2,3.14, 5]))      # correct use of sum()
print(sum_lambda(2, 3.14, 5)) # lambda

import math

circle_perimeter = lambda r: 2 * math.pi * r


sum_lambda = lambda c, p, r:  3.14 * r*r
print(sum([3.14,5 ,5]))
print(sum_lambda( 3.14,5, 5)) # lambda
"""
#map
numbers = [1,3,5,7,9]
doubled = list(map(lambda x : x*2, numbers))

print(doubled)

#filter
more_numbers = range(1,10)
evens = list(filter(lambda x: x % 2 == 0,more_numbers))
odds = list(filter(lambda x: x % 2 != 0,more_numbers))

print(evens)
print (odds)