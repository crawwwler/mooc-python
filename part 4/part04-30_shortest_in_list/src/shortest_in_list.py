def shortest(list : list) -> str :
    length = len(list[0])
    word = list[0]
    for i in list :
        if len(i) < length :
            length = len(i)
            word = i
    
    return word




if __name__ == "__main__" :
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)