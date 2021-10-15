#!/usr/bin/python3


#creating the file data.txt
f = open('data.txt','w')
f.write("1")
f = open('data.txt','r')
#print(f.readline())
f.close()

#editing the file to input more numbers
f = open('data.txt','w')
f.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")
f = open('data.txt','r')

for line in f:
    sum_of_two_number = int(line) + 11
#    print("The value of adding:{} + 11 is {}".format(int(line),sum_of_two_number))
    print(f"The value of adding: {int(line)} + 11 = {sum_of_two_number}")
f.close()

