
def total_fruits(**fruits):
    print("## from total_fruits function ::: ")
    total = 0
    for amount in fruits.values():
        total += amount
    return total
    print("\n \n \n")




print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7))

