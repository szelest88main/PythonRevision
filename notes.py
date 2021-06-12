# !/usr/bin/python3

from datetime import datetime

def create_or_append(line):
    file_descriptor = open('data.txt','a', encoding='utf-8')
    file_descriptor.write(line+"\n")
    file_descriptor.close()
    
def read_from_file():
    global loglist
    loglist = []
    file_descriptor = open('data.txt','r', encoding='utf-8')
    for val in file_descriptor.readlines():
        loglist.append(val)
        print(val.strip())
    file_descriptor.close()

res=""
loglist = []

def notes():
    global res
    while (res!="q"):
        res=input("add note => [ENTER], [q]uit, [s]how all notes so far, [r]ead saved data:\n")
        if(res=="s"):
            print("Notes so far:")
            for it in loglist:
                print(it.strip())
        elif(res=="r"):
            read_from_file()
        elif(res!="q"):
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            string_with_date = dt_string+"\t"+res 
            loglist.append(string_with_date+"\n")
            create_or_append(string_with_date)

def main():
    notes()

if __name__ == "__main__":
    main()