def longest(strings: list):
    x = len(strings[0])
    word = strings[0]

    for s in strings :
        if len(s) > x :
            x = len(s)
            word = s
    return word