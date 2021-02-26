
_author_ = "Avery Brinkman"
_credits_ = ["Wikipedia and Discord Server (John Whiting had a msg about the single quotes at beginning and end, and Dan who showed how to use //)"]
_email_ = "brinkmae@mail.uc.edu"

def egypt(n,d):
    """
    >>> egypt(3,4)
    '1/2 + 1/4 = 3/4 '
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12 = 11/12 '

    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424 = 103/104 '
    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112 = 123/124 '
    """
    
    newNum = n
    newDenom = d

    #List to track denominators of unit fractions
    dList = []


    while newNum != 0:

        #Replacement for ceil function to better deal w/ large numbers
        if newDenom % newNum == 0:
            unit = newDenom // newNum
        else:
            unit = (newDenom // newNum) + 1

        #Adds unit frac denom to list
        dList.append(unit)

        #Subtracts unit frac from new frac and updates values
        newNum = (newNum*unit) - newDenom
        newDenom = newDenom*unit


    #Prints the first quote
    print('\'', sep='', end='')

    #Prints each fraction w/ appropriate formatting
    for t in range(len(dList)):
        print(f"1/{dList[t]}",end="")
        if t >= len(dList)-1:
            print(f" = {n}/{d}",end="")
            break
        else:
            print(" + ",end="")

    #Prints end quote
    print(' \'', sep='', end='')


## Partial credit will be given for code that passes the two given doctests. 
## For full credit on HW1 you should test your solutions to egypt(103,104) and  egypt(123,124)
## These are more difficult and may require you to develop faster, more efficient code.

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)