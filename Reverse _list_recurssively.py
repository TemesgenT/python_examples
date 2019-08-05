def reverse(lst):
    '''lst = [1,2,3,4,5]
    for i in range(len(lst)):'''
    return  [ ] if len(lst) == 0 else  reverse(lst[1:]) + lst[0:1] #recursively push first element
print(reverse([1,2,3,4,5,6]))

'''Output
 [6, 5, 4, 3, 2, 1]'''
