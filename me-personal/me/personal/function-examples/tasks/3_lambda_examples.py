

""""""

"""
    Syntax :
        lambda argument(s) : expression 
"""



"""
    lambda function without argument
"""
greet = lambda : print('Hello World')
greet()



"""
    lambda function with argument
"""
sum_fun = lambda x,y : x+y
print(sum_fun(5,6))


"""
    lambda function with if else
"""
max_val = lambda x,y : x if x>y else y
print("max value between 56 , 63 is ::: ",max_val(56,63))



"""
    lambda function with for loop
"""
list_one = [10 , 20 , 30]
lambda_with_loop = lambda : [ z*2 for z in list_one ]
print(lambda_with_loop())

lambda_with_loop_and_args = lambda x , y : [ x * y * z * 2 for z in list_one ]
print(lambda_with_loop_and_args(5 , 6))


"""
    lambda function with for loop and if 
"""
list_two = [10 , 20 , 30 , 40]
lambda_with_loop_and_if = lambda : [ z*2 for z in list_one if z > 10 ]
print(lambda_with_loop_and_if())

lambda_with_loop_and_if_with_args = lambda x , y : [ x * y * z * 2 for z in list_one if z > 10]
print(lambda_with_loop_and_if_with_args(5 , 6))





"""
    lambda function with argument and filter
"""
list_of_num = [35, 12, 69, 55, 75, 14, 73]
even_list = list(filter( lambda num: (num % 2 == 0) , list_of_num ))
print("even numbers ::: ",even_list)

even_list_two = list(filter( lambda num: num if num % 2 == 0 else False , list_of_num ))
print("even numbers two ::: ",even_list_two)

odd_list = list(filter( lambda num: (num % 2 != 0) , list_of_num ))
print("odd numbers ::: ",odd_list)

odd_list_two = list(filter( lambda num: num if num % 2 != 0 else 0 , list_of_num ))
print("even numbers ::: ",odd_list_two)



"""
    lambda function with argument and map
"""
numbers_list = [4,6,8,12,16]
calulate_square_one = list(map(lambda x: x * x ,numbers_list))
print("calulate_square_one is ::: ", calulate_square_one)






"""
    lambda function with list comprehension
"""
print(" a. squares using for comprehension is ::: ")
#squares = [lambda num : num ** 2 for num in range(0, 11)]
#squares =  [lambda num = num: num ** 2 for num in range(0, 11)]
#squares = [lambda res=num: res ** 2 for num in range(0, 11)]
#squares_list = [lambda arg=x: arg * arg for x in range(0, 11)]
# squares_list = [lambda : x * x for x in range(0, 11)]
# for item in squares_list:
#     print( item)

print(" b. 10 multiples using for comprehension is ::: ")
mul_list_b = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in mul_list_b:
    print(item())


# print(" c. variable value multiples using for comprehension is ::: ")
# mul_list_c = [lambda a , b : a * b * x for x in range(1, 5)]
# for item in mul_list_c(6 , 7):
#     print(item())
#
#
# print(" d. variable value multiples using for comprehension is ::: ")
# mul_list_d = [lambda y, arg=x : arg * y for x in range(1, 5)]
# for item in mul_list_d(6):
#     print(item())



