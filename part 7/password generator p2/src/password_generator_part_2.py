import random
import string

def generate_strong_password(length: int, num: bool, pun: bool):
    ss = random.choice(string.ascii_lowercase)
    x = ''
    punc = '!?=+-()#'
    if num == False and pun == False :
        x = string.ascii_lowercase
    elif num == True and pun == False :
        ss += random.choice(string.digits)
        x = string.ascii_lowercase + string.digits
    elif num == False and pun == True :
        ss += random.choice(punc)
        x = string.ascii_lowercase + punc
    elif num == True and pun == True :
        ss += random.choice(string.digits)
        ss += random.choice(punc)
        a = string.ascii_lowercase 
        b = string.digits
        x = a + b + punc
    
    while len(ss) < length :
        ss += random.choice(x)
    return ss





if __name__ == "__main__" :
    print(generate_strong_password(6,True,True))



