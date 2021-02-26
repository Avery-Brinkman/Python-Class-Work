
_author_ = "Avery Brinkman"
_credits_ = ["https://stackabuse.com/python-how-to-flatten-list-of-lists/ (Q4)"]
_email_ = "brinkmae@mail.uc.edu"


##Lab04 Required Questions ##

#########
# Lists #
#########


# RQ1
def cascade(lst):
    """Returns the cascade of the given list using recursion.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """

    for i in range(len(lst)-1,-1,-1):
        lst.append(lst[i])
    return lst


# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """

    for i in range(0,len(seq)):
        seq[i]=fn(fn(seq[i]))
    return seq


#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """

    for i in range(len(seq)-1,-1,-1):
        if pred(seq[i]):
            del seq[i]
    return seq


#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.

    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """

    return [i for i in range(0,n) if pred(i)]


#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.

    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """

    if len(lst) == 0:
        return lst
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    return lst[:1] + flatten(lst[1:])


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)