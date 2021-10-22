#!/usr/bin/python3

i = 0
with open("example.mbox") as f:
    for l in f:
        l = l.strip()
        print("{: 02d} {}".format(i, l))
        i += 1
