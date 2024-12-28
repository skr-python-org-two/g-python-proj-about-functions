
""""""
"""
    Exone
"""
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)




"""
    Generator expression => (expression for item in iterable)
"""

# generator expression
generator_exp = (i * 5 for i in range(5) if i % 2 == 0)

for i in generator_exp:
    print(i)


