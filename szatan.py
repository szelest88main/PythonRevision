# !/usr/bin/python3

#from graphics import *
#win = GraphWin()


def create_or_append(line):
    file_descriptor = open('data.txt','a', encoding='utf-8')
    file_descriptor.write(line+"\n")
    
def read_from_file():
    file_descriptor = open('data.txt','r', encoding='utf-8')
    for val in file_descriptor.readlines():
        print(val.strip())
res=""
loglist = []

while (res!="q"):
    res=input("add note => [ENTER], [q]quit, [s]show all notes so far, [r]ead saved data:\n")
    if(res=="s"):
        
        print("Notes so far:")
        for it in loglist:
            print(it.strip())
    elif(res=="r"):
        read_from_file()
    else:
        if(res!='q'):
            loglist.append(res+"\n")
            create_or_append(res)

#val = 665

#print("Szatan: " + str(val))

#ok, let's do fizzbuzz

# for iterator in range (1,101):
#     if(iterator%3==0 and iterator%5==0):
#         print("FizzBuzz")
#     elif (iterator%3==0):
#         print("Fizz")
#     elif (iterator%5==0):
#         print("Buzz")
#     else:
#         print(str(iterator))


## loop
# for it in range(1,101):
#     print("Param " + str(it))

## if
# if (val==666):
#     print("Blaaa")
# elif (val==665):
#     print("Bluuu")
# else:
#     print("Bleee")
