#!/usr/bin/python3

# suggested time: 20 mins

# INSTRUCTIONS:
#
# Write a program that counts the number of lines in itself.  (nb: how
# many lines in this file)
#
# Hint: the program's filename is contained in the first item in
# sys.argv
#
# Print the answer.


# YOUR WORK GOES HERE.
import sys

no_of_lines = 0

with open(sys.argv[0]) as f:
    for line in f:
        no_of_lines += 1

print(no_of_lines)

