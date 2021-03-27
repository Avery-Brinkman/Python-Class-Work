_author_ = "Avery Brinkman"
_credits_ = []
_email_ = "brinkmae@mail.uc.edu"

import time

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
    print("Running function...")
    start_time = time.time()

    outWords = []
    for w in words:
        if len(w) != len(inputWord)+1:
            continue
        for cW in checkWords:
            if sorted(w) == sorted(inputWord + cW):
                outWords += [w]

    print("runtime:", time.time()-start_time)
    return outWords


print(step("APPLE"))