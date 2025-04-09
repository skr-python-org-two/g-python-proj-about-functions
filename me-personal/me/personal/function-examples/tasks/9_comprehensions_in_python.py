

""""""

"""
    List comprehension with-without if clause and with-without argument in python
"""
"""
    Syntax :- 
    newlist  = [expression for item in iterable if condition == True]
    
    Link:- https://www.w3schools.com/python/python_lists_comprehension.asp
"""

lst = [34 , 667 , 89 , 90 , 64 , 3 , 56]
list_compre = lambda : [ x*2 for x in lst ]
print(list_compre())

list_compre_two = lambda : [ x*2 for x in lst if x%2 == 0 ]
print(list_compre_two())

list_compre_three = lambda y : [ x*y for x in lst if x%2 == 0 ]
print(list_compre_three(7))

# list comprehension with for loop and only if condition
# find even_numbers:
a = range(25)
result = [n for n in a if n % 2 == 0]
print("even numbers ::: ",result)

# list comprehension with for loop and if - else
# find even or odd
a = range(25)
result = ['Even' if n % 2 == 0 else 'Odd' for n in a]
print("even or odd numbers ::: ",result)



# list comprehension with for loop and multiple if - else
# find number divisible by 2, 3 or neither:-
a = range(25)
result = ['Divisible by 2' if n % 2 == 0 else 'Divisible by 3' if n % 3 == 0 else 'Other' for n in a]
print("divisible by 2 or 3 or neither ::: ",result)

# list comprehension with multiple for loops
# print the words in geven list of sentences:-
paragraph = ["i ilke playing cricket", "i like playing football too",
             "i donot like video games", "i donot like indoor games"]
words_list = [word for sentense in paragraph for word in sentense.split(" ")]
print("words in given list of sentences" ,words_list)


# list comprehension with multiple for loops and single if - else
# print the words in geven list of sentences with even no of caracters:-
paragraph = ["i ilke playing cricket", "i like playing football too",
             "i donot like video games", "i donot like indoor games"]
words_list = [word for sentense in paragraph for word in sentense.split(" ") if len(word) % 2 == 0]
print("words in given list of sentences with even number ::: " ,words_list)

# list comprehension with multiple for loops and multiple if - else:-
# print the words with 1, 2, 3 characters in geven list of sentences:-
paragraph = ["i ilke playing cricket", "i like playing football too",
             "i donot like video games", "i donot like indoor games"]
words_list = ['one_car' if len(word) == 1 else 'even_char' if len(word) % 2 == 0 else 'odd_char'
                        if len(word) % 3 == 0 else 'other' for sentense in paragraph for word in sentense.split(" ")]
print("words with 1, 2, 3 characters in geven list of sentences  ::: ",words_list)


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

