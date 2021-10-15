

#!/usr/bin/python3


class Pet:
    """ Class about pets with name and age."""
    def  __init__(self,name,age):
        self.name = name
        self.age = age
    

    def hello(self):
        print("The name of the pet is {} and age is {} ".format(self.name,self.age))
       

pet1 = Pet("Dog",3)
pet1.hello()
pet2 = Pet("Cat",5)
pet2.hello()

