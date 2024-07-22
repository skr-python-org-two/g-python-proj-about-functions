from typing import List , Dict
def func_with_all_args(sno : int , name : str , args_list: List[int], key_args_list: Dict[str, str]):
    print("### from func_with_all_args method")
    print("type of args_list is ::: ", type(args_list))
    print("total no of arguments passed are ::: ",len(args_list))
    print("sno is ::: ", sno)
    print("name is ::: ", name)
    print("values in args_list is :::: ")
    for i in args_list:
        print("                           ",i)


    print("values in key_args_list is :::: ")
    for x,y in key_args_list.items():
        print("                           ",x,y)


func_with_all_args(1,"sekhar", args_list=[34, 78, 79], key_args_list={ "city":"machiliptnam","street_no":"2-56","pincode":"521132" })
print("\n \n \n")



def func_with_all_args_two(sno : int , name : str , args_list, key_args_list):
    print("### from func_with_all_args_two method")
    print("type of args_list is ::: ", type(args_list))
    print("total no of arguments passed are ::: ",len(args_list))
    print("sno is ::: ", sno)
    print("name is ::: ", name)
    print("values in args_list is :::: ")
    for i in args_list:
        print("                           ",i)


    print("values in key_args_list is :::: ")
    for x,y in key_args_list.items():
        print("                           ",x,y)



func_with_all_args_two(1,"sekhar", args_list=[34, 78, 79], key_args_list={ "city":"machiliptnam","street_no":"2-56","pincode":"521132" })
print("\n \n \n")







