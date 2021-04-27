# !/usr/bin/python3

res=""
loglist = []
while (res!="q"):
    res=input("add note => [ENTER], [q] to quit, [s] to show all notes so far:\n")
    if(res!="s"):
        loglist.append(res)
    else: # s
        print("Notes so far:")
        for it in loglist:
            print(it)
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
