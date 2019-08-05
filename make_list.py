# Program to produce making a list

def make_list():
    result = list() # initialize result with empty list
    in_val = 0
    while in_val >= 0:   #condition only statisfy
         in_val = int(input("Enter an int (-1 quite): "))
         if in_val >= 0:
            result += [in_val]  # add the the value in the list
    return result
def main():

    col = make_list()
    print("Here is the list ", col)
    largest = max(col)
    print("The max is:" , largest) #get the largest using max built in fuction
main()

'''The Output 
Enter an int (-1 quite): 1
Enter an int (-1 quite): 34
Enter an int (-1 quite): 5
Enter an int (-1 quite): 7
Enter an int (-1 quite): 9
Enter an int (-1 quite): 20
Enter an int (-1 quite): -1
Here is the list  [1, 34, 5, 7, 9, 20]
The max is: 34'''
