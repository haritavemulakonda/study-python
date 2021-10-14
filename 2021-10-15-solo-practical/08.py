#!/usr/bin/python3

# suggested time: 10 mins

# INSTRUCTIONS:
#
# This program requires command-line arguments.
#
# If the user calls the program without command-line arguments, have
# it call the usage() function and exit with an appropriate return
# value.
#
# Otherwise, call the main() function.

import sys

def main():
    print("main function")

def usage():
    print("the correct way to call me is: p8.py -h hello")

if len(sys.argv) <= 1:
    usage()
    exit(0)
else:
    main()
