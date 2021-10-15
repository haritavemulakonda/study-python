#!/usr/bin/python3

"""My lovely pet class"""

class MyClass:
    """don't forget docstring"""
    def say_hello(self):
        return "Hello!"

    # a constructor
    def __init__(self, miles_per_hour):
        self.a = 1
        self.b = miles_per_hour
        
class Pet:
    """a fluffy friend"""
    def speak(self):
        return self.greeting

    def __init__(self, name, age, how_to_say_hi):
        self.name = name
        self.age = age
        self.greeting = how_to_say_hi

    def about(self):
        return ("My name is "
                + self.name
                + ", and my age is "
                + str(self.age)
                + ", and I like to say "
                + self.greeting)


mypet = Pet("Cecilly", 3, "Hiss!")
print(mypet.about())
