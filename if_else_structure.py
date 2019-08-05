#Program to show how nesteled if and else structure is work

i = int(input(" i = "))
j = int(input("j = "))
k = int(input("k = "))
if i < j:
    if j < k:
        i = j     # assign value j to i
    else:
        j = k     #esle assigne value k to j
else:            # function goes when i > j
     if j >  k:
         j = i
     else:
         i = k
print("The output: i =", i, " j =", j, " k =", k)

''' ---   Output --------
The first condition ( if i < j  and j < k  then assign j value to i, )
i = 3
j = 5
k = 7
The output: i = 5  j = 5  k = 7       // j and i have same value

The second condtion output ( if i < j but if j  > k , assign k value to j)
i = 3
j = 7
k = 5
The output: i = 3  j = 5  k = 5    //  j and k have same value
The third conditon ( if i > j function check the outer else statment, if j > k, assign j to i )
i = 7
j = 5
k = 3
i = 7  j = 7  k = 3   // i and j have same value
The fourth conditon (if i > j and j < k result assing k value to i)
i = 7
j = 3
k = 5
The output: i = 5  j = 3  k = 5   // i and k have same value '''
