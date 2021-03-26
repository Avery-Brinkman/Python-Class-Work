_author_ = "Avery Brinkman"
_credits_ = []
_email_ = "brinkmae@mail.uc.edu"

# Provided code
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

def step(inputWord):
    print("Running function...")
    checkWords = []
    outWords = []
    for i in range(65, 91):
        checkWords.append(inputWord + chr(i))
    for w in words:
        for cW in checkWords:
            if sorted(w) == sorted(cW):
                outWords += [w]
    return outWords

print(step("APPLE"))