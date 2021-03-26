_author_ = "Avery Brinkman"
_credits_ = []
_email_ = "brinkmae@mail.uc.edu"

## Mutables Linked Lists ##

# RQ1
def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """

    out = []
    if link == 'empty list':
        return out
    for i in range(len(link)):
        out += [link[i]]
    return out
    

# RQ2
def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> print(link)
    Link(1, Link(2, Link(3)))
    """
    if len(lst) == 1:
        return Link(lst[0])
    return Link(lst[0], list_to_link(lst[1:]))
    


# RQ3
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    Link(9, Link(Link(16), Link(25, Link(36))))
    """
    if isinstance(link.first, Link):
        deep_map_mut(fn, link.first)
    else:
        link.first = fn(link[0])
    if link.rest != Link.empty:
        deep_map_mut(fn, link.rest)
    



# RQ4
def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> insert(link, 9001, 0)
    >>> print(link)
    Link(9001, Link(1, Link(2, Link(3))))
    >>> insert(link, 100, 2)
    >>> print(link)
    Link(9001, Link(1, Link(100, Link(2, Link(3)))))
    >>> insert(link, 4, 5)
    Traceback (most recent call last):
    ...
    IndexError
    """
    if index >= len(link):
        raise IndexError
    if index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    else:
        insert(link.rest, value, index-1)

class Link:
  empty = 'empty list'
  
  def __init__(self, first, rest=empty):
    assert rest is Link.empty or isinstance(rest, Link)
    self.first = first
    self.rest = rest
  
  def __len__(self):
    if self.rest == Link.empty:
      return 1
    else:
      return 1 + len(self.rest)
  
  def __getitem__(self, index):
    if index == 0:
      return self.first
    else:
      return self.rest[index-1]
  
  def __repr__(self):
    if self.rest == Link.empty:
      repstr = ''
    else:
      repstr=", " + Link.__repr__(self.rest)
    return 'Link({0}{1})'.format(self.first, repstr) 
  
  def __add__(self, other):
    assert other is Link.empty or isinstance(other, Link)
    if self == Link.empty:
      return other
    else:
      return Link(self.first, Link.__add__(self.rest, other))

import doctest
if __name__ == '__main__':
    doctest.testmod(verbose=True)
