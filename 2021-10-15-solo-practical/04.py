#!/usr/bin/python3

# suggested time: 10 mins

# INSTRUCTIONS
#
# Create a basic class called MixItUp.
#
# The class has a function called "hi", which prints "hi".
#
# The class has a function called "multiply", which multiplies the two
# supplied arguments.  It returns the result.
#
# Create one instance.  Write code that demonstrates the features you
# have written.


# YOUR WORK GOES HERE.


class MixItUp:

    def hi(self):
        print("hi")


    def multiply(self,arg1,arg2):
        return arg1 * arg2

g1 = MixItUp()
g1.hi()
print(g1.multiply(2,3))





