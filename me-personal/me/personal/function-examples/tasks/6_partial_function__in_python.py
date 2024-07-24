from functools import *


# A normal function
def add(a, b, c):
    return 100 * a + 10 * b + c


# A partial function with b = 1 and c = 2
add_part = partial(add, c=2, b=1)

# Calling partial function
print(add_part(3))




# original function
def power(exponent, base):
    return base ** exponent
#Partial function
square = partial(power, 2) # setting value of exponent to 2
cube = partial(power, 3) # setting value of exponent to 3
# Calling Partial function
print("The square of 5 is", square(5))
print("The cube of 7 is", cube(7))



# original function
def print_msg(name, message):
    msg = str(name) +", "+ str(message)
    return msg
#Partial function
welcome = partial(print_msg, message='Welcome to the Team!') #setting the welcome message
holidays = partial(print_msg, message='Happy Holidays!')
# Calling Partial function
print(welcome('Sourish'))
print(holidays('Shubhrima'))


