#Program to produce statistic histograph  taking both the items and its occurance in the data using dictionary

def countTheNumberofItems():
    word = "Temesgen_gebremicheal_Tesfay"
    d = dict() #initialize count with dictionary hold both the count as key and the value
    for c in word :    # c is an element of word
        if c not in d :  # if c is not duplicated in d (dictionalry)
             d[c ] =  1  # then assign dictionary of specific item  one,(not duplicated)
        else:
            d[c] = d[c] + 1  # else if same items are repreated then add one to each items count and updated the
            #count in accumlator left side variable.

    print(d)
if __name__ == '__main__':
    countTheNumberofItems()

'''The Output 
{'T': 2, 'e': 7, 'm': 2, 's': 2, 'g': 2, 'n': 1, '_': 2, 'b': 1, 'r': 1, 'i': 1, 'c': 1, 'h': 1, 'a': 2, 'l': 1, 'f': 1, 'y': 1}
'''
