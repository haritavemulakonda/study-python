#!/usr/bin/python3

class House:

    def __init__(self):
        self.address = None
        self.no_of_windows = None
        self.no_of_doors = None

    """This is for printing the house details"""
    def p_out(self):
        print(f"This house has {self.no_of_windows} windows, has {self.no_of_doors} doors and is located at : {self.address}") 


    def set_address(self, address):
        self.address = address


    def set_windows(self, no_of_windows):
        self.no_of_windows = no_of_windows


    def set_doors(self, no_of_doors):
        if isinstance(no_of_doors,int):
            self.no_of_doors = no_of_doors
        else:
            raise ValueError("Invalid number provided!")


    def set_lock(self):
        self.door_lock = True
        print("The doors are now locked")


    def set_unlock(self):
        self.door_lock = False
        print("The doors are now open")


    def enter(self):
        if self.door_lock:
            print("The door is locked")
        else:
            print("Open the door and enter!")








