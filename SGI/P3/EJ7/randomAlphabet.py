import string
import random

def randomAlphabet():

    l = list(string.ascii_lowercase)

    random.shuffle(l)
    result = ''.join(l)

    return result

if __name__ == "__main__":
    
    randomAlphabet()