


p="global"


"""
    Refering global variable p inside inner-function
"""
def outerthree():
    x = "local"

    def inner():
        nonlocal x
        global p
        x = "nonlocal"
        p = "nonlocal"
        print("inner x:", x)
        print("inner p:", x)

    inner()
    print("outer x:", x)

outerthree()
print("outer p:", p)


p="global"

"""
    creating local  variable p inside inner-function
"""
def outerfour():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        p = "nonlocal"
        print("inner x:", x)
        print("inner p:", x)

    inner()
    print("outer x:", x)

outerfour()
print("outer p:", p)
