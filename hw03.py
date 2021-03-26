_author_ = "Avery Brinkman"
_credits_ = []
_email_ = "brinkmae@mail.uc.edu"

# Provided code
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

