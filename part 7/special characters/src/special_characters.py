import string

def separate_characters(my_string: str):
    string1 = ""
    string2 = ""
    string3 = ""

    for c in my_string :
        if c in string.ascii_letters :
            string1 = string1 + c
        elif c in string.punctuation :
            string2 = string2 + c
        else :
            string3 = string3 + c
    
    return (string1, string2, string3)






