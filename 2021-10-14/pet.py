#!/usr/bin/python3

"""My lovely pet class"""

class Pet:
    """a fluffy friend"""
    counter = 0

    def speak(self):
        return self.greeting

    def __init__(self, name, age, how_to_say_hi):
        self.name = name
        self.age = age
        self.greeting = how_to_say_hi
        Pet.counter += 1

    def total_instance(self):
        return Pet.counter


    def about(self):
        return ("My name is "
                + self.name
                + ", and my age is "
                + str(self.age)
                + ", and I like to say "
                + self.greeting)



cecilly = Pet("Cecilly", 3, "Hiss!")
print(cecilly.about())
print(cecilly.total_instance())

toro = Pet("Toro", 6, "Meowww")
print(toro.about())
print(toro.total_instance())

happy = Pet("Happy", 2, "Hi")
print(happy.about())
print(happy.total_instance())

joy = Pet("Joy", 8, "JJ")
print(joy.about())
print(joy.total_instance())

my_pet_family = []
for p in [cecilly.name,toro.name,happy.name,joy.name]:
    my_pet_family.append(p)
my_pet_family.sort()

print("My pet family:{}".format(my_pet_family))



