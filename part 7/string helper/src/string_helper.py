import string

def change_case(orig_string: str):
    new_orig = ''
    for w in orig_string :
        if w.isupper() :
            w = w.lower()
        else :
            w = w.upper()
        new_orig += w
    return new_orig


def split_in_half(orig_string: str):
    if len(orig_string) % 2 == 0 :
        p = len(orig_string) / 2
    else :
        p = len(orig_string) // 2
    p = int(p)
    return (orig_string[:p], orig_string[p:])


def remove_special_characters(orig_string: str):
    new_orig = ''
    for w in orig_string :
        if not(w in string.ascii_letters or w in string.digits or w == " "):
            w = ''
        new_orig += w
    return new_orig



if __name__ == "__main__" :
    x = remove_special_characters("veji4r9wejfpmf 4t903fc 3490c ! !! $ @KOR$ fg")
    print(x)



                           