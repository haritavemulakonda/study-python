#!/usr/bin/python3

# suggested time: 10 mins

# INSTRUCTIONS:
#
# Improve this program so that it exits gracefully (and silently) when
# the user cancels input with Ctrl-C.

accumulator = 0
try:
    while True:
        v = input("Number to add? ")
        accumulator += int(v)
        print("accumulator at ", accumulator)
except:
    print("Smooth Exit")

