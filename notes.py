# !/usr/bin/python3

from datetime import datetime

# append the line to the 'data.txt' file 
# or create the file first it it doesn't exist
def create_or_append(line):
    file_descriptor = open('data.txt','a', encoding='utf-8')
    file_descriptor.write(line+"\n")
    file_descriptor.close()
    
logs_list = []

# read all the lines from 'data.txt', 
# print them to screen and add them to logs_list list.
def read_from_file():
    global logs_list # "global": don't override the global logs_list: use it 
    logs_list = []
    file_descriptor = open('data.txt','r', encoding='utf-8')
    for val in file_descriptor.readlines():
        logs_list.append(val)
        print(val.strip())
    file_descriptor.close()


def notes():
    res=""
    while (res!="q"):
        res=input('add note => [ENTER], [q]uit, [s]how '
        'all notes so far, [r]ead saved data:\n')
        if(res=="s"):
            print("Notes so far:")
            for it in logs_list:
                print(it.strip())
        elif(res=="r"):
            read_from_file()
        elif(res!="q"):
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            string_with_date = dt_string+"\t"+res 
            logs_list.append(string_with_date+"\n")
            create_or_append(string_with_date)

def main():
    notes()

if __name__ == "__main__":
    main()