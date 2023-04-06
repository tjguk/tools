import os, sys
import random
import string

def generate(n_chars=12):
    return "".join(random.choices(string.ascii_letters + string.digits, k=int(n_chars)))

if __name__ == '__main__':
    print(generate(*sys.argv[1:]))
