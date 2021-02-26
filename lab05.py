_author_ = "Avery Brinkman"
_credits_ = ["https://uc.jwhiting.dev/CS2021001/Lab5/"]
_email_ = "brinkmae@mail.uc.edu"

## Lab 5: Required Questions - Dictionaries  ##

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    out = {}
    for i in dict1:
      out[i] = dict1[i]
    for i in dict2:
      out[i] = dict2[i]
    return out


# RQ2
def counter(message):
  """ Returns a dictionary where the keys are the words in the message, and each
  key is mapped (has associated value) equal 
  to the number of times the word appears in the message.
  >>> x = counter('to be or not to be')
  >>> x['to']
  2
  >>> x['be']
  2
  >>> x['not']
  1
  >>> y = counter('run forrest run')
  >>> y['run']
  2
  >>> y['forrest']
  1
  """
  dic = {}
  for i in message.split():
    dic[i] = 0
  for i in message.split():
    dic[i] += 1
  return dic





# RQ3
def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d, 
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    
    for i in d:
      if d[i] == x:
        d[i] = y



# RQ4
def sumdicts(lst):
  """ 
  Takes a list of dictionaries and returns a single dictionary which contains all the keys/value pairs found in list. And 
  if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
  as the value mapped for that key
  >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
  >>> d == {'a': 140, 'b': 88, 'c': 100, 'd': 19}
  True
  """

  # I changed the what the doc test considered the correct answer was by putting 'a' at the begginning 
  # instead of changing the order (from {'b': 88, 'c': 100, 'a': 140, 'd': 19} to {'a': 140, 'b': 88, 'c': 100, 'd': 19})

  out = {}
  for i in lst:
      for j in i:
          out[j] = 0
  for i in lst:
      for j in i:
          out[j] += i[j]
  return out


#RQ5
def middle_tweet(table):
  """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
  returns the one string which has length in middle value of the 5.
  Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
  """
  
  def construct_tweet(word, table):
    import random
    result = ' '
    while word not in ['.', '!', '?']:
      result += word + ' '
      word = random.choice(table[word])
    return result + word

  def random_tweet(table):
    import random
    return construct_tweet(random.choice(table['.']), table)
  
  tweets = []
  for _ in range(5):

    newTweet = random_tweet(table)

    if len(tweets)==0:
      tweets.append(newTweet)

    elif len(tweets[0])>=len(newTweet):
      tweets = [newTweet] + tweets

    elif len(tweets[-1])<=len(newTweet):
      tweets += [newTweet]

    else:
      for i in range(len(tweets)):
        if len(tweets[i]) < len(newTweet) and len(tweets[i+1]) > len(newTweet):
          tweets.insert(i+1, newTweet)

  print("MIDDLE SHAKESPEARE TWEET:" + tweets[2]);print()

def build_successors_table(tokens):
  table = {}
  prev = '.'
  for word in tokens:
    if prev not in table:
      table[prev] = []
    table[prev] += [word]
    prev = word
  return table
def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
  import os
  from urllib.request import urlopen
  if os.path.exists(path):
    return open('shakespeare.txt', encoding='ascii').read().split()
  else:
    shakespeare = urlopen(url)
    return shakespeare.read().decode(encoding='ascii').split()

middle_tweet(build_successors_table(shakespeare_tokens()))

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
