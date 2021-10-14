#!/usr/bin/python3

# INSTRUCTIONS:
#
# Complete the following functions, ensuring they furfil the
# specifications given in the docstrings.  Functions must work to
# specification with the given function calls.

# suggested time: 15 mins

print("=== say_hello ===")
def say_hello(name):
    """Takes name supplied as argument, and prints 'Hi name'"""
    # example: if given "Toby", prints "Hi Toby"
    print(f"Hi {name}")

say_hello("Toby")


print("\n=== date_check ===")
def date_check(year, day):
    """Returns a boolean if it is after the year 2000, and the day is
'Friday'"""
    # example: a Tuesday in 1980 is False, a Friday in 2021 is True
    if year > 2000 and day.lower() == "friday":
        return True 
    else:
        return False

print("1980 Tuesday", date_check(1980, "Tuesday"))
print("2021 Friday ", date_check(2021, "Friday"))
print("1988 Friday ", date_check(1988, "Friday"))
print("2021 Monday ", date_check(2021, "Monday"))


print("\n=== repeater ===")
def repeater(string, repetitions):
    """Return a string that contains given string, repeated repetitions
times"""
    # nb: you must use a "for loop"
    repeating_word = ""
    for repetition in range(repetitions):
        repeating_word += string
    return repeating_word

print(repeater("Wow", 5))


print("\n=== camels ===")
def camels():
    """Ask the user "How many camels fit in a tent?".  Returns an
integer."""
    no_of_camels = input("How many camels fit in a tent?")
    return int(no_of_camels)
    
    
print("Number of camels to purchase:", camels() + 0)


print("\n=== adder ===")
def adder(collection):
    """Add the numbers supplied in collection.  Return result."""
    sum_of_collections = 0
    for numbers in collection:
        sum_of_collections += numbers
    return sum_of_collections

print(adder((1,2,3)))
