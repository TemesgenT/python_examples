#programm to find the prime numbers
def is_prime():
    max_val = int(input("Enter maximum value: "))
    value = 2  # smallest prime number

    while value <= max_val:
          ''' check number is prime'''
          is_prime = True
          factor = 2
          while factor < value:
              if value % factor == 0:
                  is_prime = False
                  break   # found factor
              factor += 1 #increament the factor by one inside the nestled loop
          if is_prime:   #when inner loop did not find factor then the outer loop define the number is prime
             print(value, end=' ')
          value += 1 #increment the value by one on the outer loop to check next number is prime
    print()
if __name__ == '__main__':
    is_prime()
''' Output 
Enter maximum value: 20
2 3 5 7 11 13 17 19 
'''
