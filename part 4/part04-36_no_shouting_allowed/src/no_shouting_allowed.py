def no_shouting(words : list) -> list :
    new_words = []
    for w in words :
        if w.isupper() == True :
            continue
        else :
            new_words.append(w)
    
    return new_words
