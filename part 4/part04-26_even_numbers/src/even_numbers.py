def even_numbers(list : list) -> list :
    list_to_return = []
    for i in list :
        if i % 2 == 0 :
            list_to_return.append(i)
    return list_to_return