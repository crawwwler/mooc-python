def distinct_numbers(list : list ) -> list :
    new_list = []
    for i in list :
        if not(i in new_list):
            new_list.append(i)
    new_list.sort()
    return new_list




if __name__ == "__main__" :
    my_list = [1, 3, 6, 7, 8, 9, 10]
    print(distinct_numbers(my_list)) # [1, 2, 3]
