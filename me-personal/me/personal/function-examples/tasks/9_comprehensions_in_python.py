

""""""

"""
    List comprehension with-without if clause and with-without argument in python
"""

lst = [34 , 667 , 89 , 90 , 64 , 3 , 56]
list_compre = lambda : [ x*2 for x in lst ]
print(list_compre())

list_compre_two = lambda : [ x*2 for x in lst if x%2 == 0 ]
print(list_compre_two())

list_compre_three = lambda y : [ x*y for x in lst if x%2 == 0 ]
print(list_compre_three(7))


"""
    Dictionary comprehension with-without if clause and with-without argument in python
"""
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

myDict = lambda : { k:v for (k,v) in zip(keys, values)}
print (myDict())

myDict_two =  lambda : { k:v for (k,v) in zip(keys, values) if v%2 == 0}
print (myDict_two())

myDict_three =  lambda : { k:v*2 for (k,v) in zip(keys, values) if v%2 == 0}
print (myDict_three())

myDict_four =  lambda y : { k:v*y for (k,v) in zip(keys, values) if v%2 == 0}
print (myDict_four(6))

