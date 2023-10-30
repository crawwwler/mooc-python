def everything_reversed(words : list) -> list :
    words = words[::-1]
    new_words = []
    for w in words :
        w = w[::-1]
        new_words.append(w)
    
    return new_words





if __name__ == "__main__" :
    
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
