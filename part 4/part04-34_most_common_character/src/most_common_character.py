def most_common_character(word : str) -> str :
    x = 1
    w = ""
    for c in word :
        n = word.count(c)
        if n > x :
            x = n 
            w = c
    return w