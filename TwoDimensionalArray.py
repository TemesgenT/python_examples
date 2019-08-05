#program to produce how loop work from inside to outer loop

def tree(height):
    row = 0  # first row keep index[0]
    while row < height:   #outer loop condition
        count = 0
        while count < height - row:
            print(end="  ")    #print number of blanks
            count += 1

        count_1 = 0
        while count_1 < 2 * row + 1  :
            print(end="*")   # put one * in first row and 3 on the second, and  keep the trend until the outer loop condition is false
            count_1 += 1    #number of asteries grows twice plus 1 as row increament by one so each row have two more stars
        print()  # newline
        row += 1 # increment the row and test the outerloop condtion


height = int(input("Enter the tree height: "))
tree(height)
''' Output 
Enter the tree height: 6
      *
     ***
    *****
   *******
  *********
 ***********
 '''
