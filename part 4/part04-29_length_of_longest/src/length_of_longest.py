def length_of_longest(list : list) -> int :
    helper = len(list[0])
    for i in list :
        if len(i) > helper :
            helper = len(i)
    
    return helper