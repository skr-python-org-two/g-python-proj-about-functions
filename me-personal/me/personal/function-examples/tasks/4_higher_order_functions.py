
""""""
"""
    Assigning function to a variable
"""


# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()


print(shout('Hello'))

# Assigning function to a variable
yell = shout
print(yell('Hello'))

"""
    Passing function as function-argument
"""
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function \
    passed as an argument.")
    print(greeting)


greet(shout)
greet(whisper)


# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x + y

    return adder

add_15 = create_adder(15)
print(add_15(10))



