#!/usr/bin/python3

import os
import time


def child():
    print(f"\nI am a child:{os.getpid()}")
    time.sleep(5)
    print("\n Goodbye.  ", os.getpid())
    os. _exit(0)

def parent():
    while True:
        newpid = os.fork()
        print(f"New pid ----> {newpid}")

        if newpid == 0:
            print(f"In the child if {newpid}") 
            child()
        else:
            print(f"I am Parent with PID:{os.getpid()} child process is: {newpid}")

        reply = input("Enter for new child: 'q' to quit:")
        if reply == 'q':
            break

parent()
print("\n I am parent. BYeee")
