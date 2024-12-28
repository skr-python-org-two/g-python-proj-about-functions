

""""""
"""
    Refering non-local x variable inside inner-function
"""
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()


"""
    creating local-variable x with same name as non-local-variable as x
"""
def outertwo():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outertwo()



