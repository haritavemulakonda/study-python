#!/usr/bin/python3

import os
import time


def child():
    print(f"\nI am a child:{os.getpid()}")
    time.sleep(5)
    try:
        while not os.path.exists('newfile'):
            time.sleep(5)

        if os.path.isfile('newfile'):
            print("File is now created")
            with open("newfile","r") as f:
                s = f.read()
                print(f"Contents of the file:{s}")
            print("\n Goodbye.  ", os.getpid())
            os. _exit(0)

    except ValueError:
         print("This isn't a file!" % newfile)

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
