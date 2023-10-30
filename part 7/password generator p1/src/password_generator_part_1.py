import random
import string

def generate_password(length: int):
    ss = ''
    x = random.sample(string.ascii_lowercase, length)
    random.shuffle(x)
    for c in x :
        ss += c
    
    return ss

