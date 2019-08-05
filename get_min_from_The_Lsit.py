#Python Program to find the min value in a list without min built in function

def getMin():
    sum = 0.0
    No_of_Enteries = 5    #The number of Enteries
    print("Please enter ",No_of_Enteries, "numbers")
    smallest = None #initialzie the smallest
    for i in range(0, No_of_Enteries):
        num = float(input("Enter the number  " +  str(i + 1) +  ': '))
        if smallest is None or num   < smallest:
            smallest = num    #update the smallest
    print( "The smallest number is:  ", smallest)
if __name__ == "__main__":
    getMin()

'''Program Output 
Please enter  5 numbers
Enter the number  1: 5
Enter the number  2: -2
Enter the number  3: 7
Enter the number  4: 30
Enter the number  5: 78
The smallest number is:   -2.0
'''
