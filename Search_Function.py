import re
def findWord():
    name = input("Enter a file name: ")
    try:
        fhand = open( name, 'r') # mode of the funciton is to open and read
    except:
        print("the couldn't open", name)  #indicate error
        exit()
    for line in fhand:
        line = line.rstrip() #rstrip is built in fuction which revmove empty space in a line
        if re.search("From", line ): # if the line start with "From' print the line as whole
            print(line)

if __name__== '__main__':
    findWord()
'''OutPut
Enter a file name: C:\Users\me\Documents\TheEarth.txt
From Wikipedia, the free encyclopedia
From Temesgen Gebremicheal Tesfay
'''
