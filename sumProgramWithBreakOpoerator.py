#program to produce the sum of nonnegative numbers enteries using break operator
entery = 0    #initialize the entery'''
sum = 0        #"initialze sume "

print("Enter numbers to be sumed, if number is negative end of the list")

while True:  #boolean conditon for entery domain
    entery = int(input('Enter the number: '))
    if entery < 0:
        break
    sum += entery
print(" sum = ", sum)
''' - -----'Output ----- 
Enter numbers to be sumed, if number is negative end of the list
Enter the number: 2
Enter the number: 3
Enter the number: 5
Enter the number: 7
Enter the number: -5   // The program terminate the loop for negative number and return the sum of the enteries 
 sum =  17   
 '''
