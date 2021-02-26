"""Four Required questions for Lab 1."""
## Modify this file by adding your code. Once you pass all the doctests, 
# you can then submit you program for credit. 

_author_ = "Avery Brinkman"
_credits_ = ["w3schools.com/python"]
_email_ = "brinkmae@mail.uc.edu" # Your email address

# RQ1
def both_negative(x, y):
    """Returns True if both x and y are negative.
 
    >>> both_negative(-1, 1)
    False
    >>> both_negative(1, 2)
    False
    >>> both_negative(-1, -2)
    True
    """
    if x < 0 and y < 0:
        return True
        
    else:
        return False

# RQ2
## use while Loops ##
def not_factor (n):
    """Prints out all of the numbers that do not divide `n` evenly.
 
    >>> not_factor(10)
    9
    8
    7
    6
    4
    3
    """

    """
    for i in range(n,1,-1):
       if n % i != 0:
           print(i)
    """

    i = n

    while i > 1:
        if n % i != 0:

            print(i)

        i -= 1
 
# RQ3
def lucas(n):
    """Returns the nth Lucas number.
      Lucas numbers form a series similar to Fibonacci:
      2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843,...
 
    >>> lucas(0)
    2
    >>> lucas(1)
    1
    >>> lucas(2)
    3
    >>> lucas(3)
    4
    >>> lucas(11)
    199
    >>> lucas(100)
    792070839848372253127
    """

    ln0 = 2
    ln1 = 1
    temp = 0

    if n == 0:
        print(ln0)

    elif n == 1:
        print(ln1)

    else:
        for i in range(1,n):

            temp = ln1
            ln1 = ln0 + ln1
            ln0 = temp

        print(ln1)

#RQ4
def gets_discount(p1, p2, p3):
    """ Returns True if p1 is an adult (age at least 18) and p2 and p3 are both children (age 12 or below), 
    False otherwise. Do not use if statement.
    >>> gets_discount(15, 12, 11)
    False
    >>> gets_discount(90, 7, 12)
    True
    >>> gets_discount(18, 18, 18)
    False
    >>> gets_discount(40, 7, 15)
    False
    """

    return (p1 >= 18) and (p2 <=12 and p3 <=12)

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
