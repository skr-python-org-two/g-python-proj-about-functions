


class Wishes:
       def __init__(self,greet_message:str):
           self.message = greet_message

       def __str__(self):
           print("from sekhar")

       def wishHim(self):
            print(self.message)


x = Wishes("ghow are you")
x.wishHim()

print(x.__str__())