#Program to produce floating point comparison for it is hard or impossible to two floating point numbsers
#to have equal values

from math import fabs    # from maths module import absulute value function list
def comparTwoFloatingNumbers(a, b, tolerance ):
    return a == b or fabs(a - b) < tolerance

def main():
    i = 0.0
    while not comparTwoFloatingNumbers(i, 1.0, 0.0001):
        print(" i = ", i )  #print i until the differene between  a and b equals to 0.0001(tolerance)
        i += 0.1
        print(' toleracne = ', 1 - i)

main()
'''i =  0.0
 toleracne =  0.9
 i =  0.1
 toleracne =  0.8
 i =  0.2
 toleracne =  0.7
 i =  0.30000000000000004
 toleracne =  0.6
 i =  0.4
 toleracne =  0.5
 i =  0.5
 toleracne =  0.4
 i =  0.6
 toleracne =  0.30000000000000004
 i =  0.7
 toleracne =  0.20000000000000007
 i =  0.7999999999999999
 toleracne =  0.10000000000000009  # tolerance value still greater than the tolerance value provided for function 
 #parameter
 i =  0.8999999999999999  # The max i value which close to 1.0  accroding to the magnitude of the tolerance
 toleracne =  1.1102230246251565e-16  // the loop terminate for fabs(a - b) < toleracne 
'''
