_author_ = "Avery Brinkman"
_credits_ = []
_email_ = "brinkmae@mail.uc.edu"


# Provided code
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

checkWords = []
for i in range(65, 91):
    checkWords.append(chr(i))

def step(inputWord):

    outWords = []
    for w in words:

        if len(w) != len(inputWord)+1:
            continue

        for cW in checkWords:

            if cW not in w:
                continue

            if sorted(w) == sorted(inputWord + cW):
                outWords += [w]

    return outWords

print(step("APPLE"))

# The main issue with my code is that it runs around 235886*26 loops per comparison since it 
# makes a niave array search. I was unsure how else to go about the search even after saving 
# my copy to my GitHub on Friday and trying to think about it all weekend (which caused me to 
# forget I hadn't actually turned it in, hence the lateness). In an attempt to cut down on 
# some of these comparisons, I first check that the dictionary word is the correct length for 
# my step word. There is no need to loop through and individually add each letter of the 
# alphabet to a word when and check that it's equal to a word thats only 2 letters long. After 
# that, I check that the letter that's being added is in the dictionary word to begin with. I 
# don't need to make a whole comparison and then write data to an array. These two checks weren't 
# enough to make this a very efficient solution to the problem, but they did help cut down the time 
# to under a second (for APPLE, other words can still take slightly over 2 seconds but were still 
# improved). Making comparisons for all 235886 words is the biggest issue and the one I was unable 
# to solve. Checking the length to skip the 26 solutions was the most helpful, but wasn't the best 
# compared to the bigger picture.
# File History: https://github.com/Avery-Brinkman/Python-Class-Work/blob/master/hw03.py