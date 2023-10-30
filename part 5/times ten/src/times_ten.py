def times_ten(start_index: int, end_index: int):
    dic = {}
    for i in range(start_index, end_index+1):
        dic[i] = i*10
    return dic
    