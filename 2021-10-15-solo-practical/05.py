#!/usr/bin/python3

# suggested time: 15 mins

# INSTRUCTIONS:
#
# Improve the class, giving it a class variable that remembers the
# most-recently-instantiated name.
#
# Give your class a function called "most_recent" that returns the
# most recently instantiated name.
#
# Write code that demonstrates this functionality.

class Person:
    """About a person"""
    most_recent_name = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.most_recent_name = name

    def age_after_years(self,years_in_future):
        return self.age + years_in_future

    def most_recent(self):
        return Person.most_recent_name


p1 = Person("Tom", 21)
p2 = Person("Dick", 11)
p3 = Person("Harry", 5)

print(p1.most_recent())


