
def show_non_key_args_one(*args_list):
    print("### from show_non_key_args_one method")
    print("type of args_list is ::: ", type(args_list))
    print("total no of arguments passed are ::: ",len(args_list))
    for i in args_list:
        print("arg to function c_add is :::: ",i)

show_non_key_args_one(5,6,"sekhar",{"sno":1,"name":"sekhar"})
print("\n \n \n")


def show_non_key_args_two(a:int,b:int,*c):
    print("### from show_non_key_args_two method")
    print("a ::: ",a)
    print("b ::: ",b)
    print("c ::: ",c)

show_non_key_args_two(5,6,"sekhar",{"sno":1,"name":"sekhar"})


