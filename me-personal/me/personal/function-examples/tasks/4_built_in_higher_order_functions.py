

""""""

"""
    map , filter , reduce 
"""

"""
    Normal Higher Order Function
"""
def apply_to_each(func, iterable):
    return [func(x) for x in iterable]

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_to_each(square, numbers)
print(squared_numbers) # Output: [1, 4, 9, 16, 25]


"""
    Using map
"""
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]



"""
    Using filter
"""
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers) # [2, 4]

"""
    Using reduce
"""

from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers) # 15



