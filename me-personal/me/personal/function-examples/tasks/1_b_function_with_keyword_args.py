
def total_fruits(**fruits):
    print("## from total_fruits function ::: ")
    total = 0
    for amount in fruits.values():
        total += amount
    return total




print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7))




"""
    Method to acees keys
"""

def access_keys_of_dict(**fruits):
    print("## from access_keys_of_dict function ::: ")
    print(fruits)
    for key_val in fruits.keys():
            print("###" , key_val.upper())
    print("\n")


access_keys_of_dict(banana=5, mango=7, apple=8)
access_keys_of_dict(banana=5, mango=7, apple=8, oranges=10)
access_keys_of_dict(banana=5, mango=7)



"""
    Method to acees values
"""

def access_values_of_dict(**fruits):
    print("## from access_values_of_dict function ::: ")
    for key_val in fruits.values():
            print(key_val)
    print("\n")


access_values_of_dict(banana=5, mango=7, apple=8)
access_values_of_dict(banana=5, mango=7, apple=8, oranges=10)
access_values_of_dict(banana=5, mango=7)




"""
    Method to acees keys and values
"""
def access_key_values_of_dict(**fruits):
    print("## from access_key_values_of_dict function ::: ")
    for key , vall in fruits.items():
            print(key , vall)
    print("\n \n \n")


access_key_values_of_dict(banana=5, mango=7, apple=8)
access_key_values_of_dict(banana=5, mango=7, apple=8, oranges=10)
access_key_values_of_dict(banana=5, mango=7)




